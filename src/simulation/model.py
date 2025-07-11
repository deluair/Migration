import mesa
from ..agents.individual import IndividualAgent
from ..agents.firm import FirmAgent
from ..agents.regional import RegionalAgent
from ..agents.government import GovernmentAgent
from ..utils.data_generator import generate_individual_data, generate_firm_data, generate_regional_data
from .job_market import JobVacancy

def compute_employed(model):
    """Helper function to compute the number of employed agents."""
    return sum([1 for agent in model.schedule.agents if isinstance(agent, IndividualAgent) and agent.is_employed])

class MigrationModel(mesa.Model):
    """
    The main model for the AI-driven economic displacement and migration simulation.
    """
    def __init__(self, n_individuals, n_firms, n_regions, n_governments):
        super().__init__()
        self.num_individuals = n_individuals
        self.num_firms = n_firms
        self.num_regions = n_regions
        self.num_governments = n_governments
        self.schedule = mesa.time.RandomActivation(self)
        self.job_board = [] # Central list for job vacancies
        self.agent_id_map = {} # Helper to find agents by ID

        # Create agents
        # In the future, this will be replaced with realistic data generation
        self.datacollector = mesa.DataCollector(
            model_reporters={"Employed": compute_employed},
            # Use getattr to safely access attributes that may not exist on all agents
            agent_reporters={
                "Age": lambda a: getattr(a, 'age', None),
                "Education": lambda a: getattr(a, 'education', None),
                "MSA": lambda a: getattr(a, 'current_msa', None),
                "IsEmployed": lambda a: int(getattr(a, 'is_employed', 0)) if isinstance(a, IndividualAgent) else None
            }
        )

        # Create regions
        regional_data = generate_regional_data(self.num_regions)
        self._create_regions(regional_data)
        region_ids = [data['unique_id'] for data in regional_data]

        # Create firms
        firm_data = generate_firm_data(self.num_firms, region_ids)
        self._create_firms(firm_data)

        # Create individuals and assign them to firms
        individual_data = generate_individual_data(self.num_individuals, region_ids)
        self._create_individuals(individual_data)

        # Create governments
        self._create_governments()

    def _create_individuals(self, individual_data):
        firm_agents = [agent for agent in self.schedule.agents if isinstance(agent, FirmAgent)]
        for i, data in enumerate(individual_data):
            # Assign individuals to firms in a round-robin fashion
            employer = firm_agents[i % len(firm_agents)]
            data['employer_id'] = employer.unique_id

            agent = IndividualAgent(self.next_id(), self, **data)
            self.schedule.add(agent)
            self.agent_id_map[agent.unique_id] = agent

            # Add employee to firm's list
            employer.employees.append(agent.unique_id)


    def _create_firms(self, firm_data):
        for data in firm_data:
            agent = FirmAgent(self.next_id(), self, **data)
            self.schedule.add(agent)
            self.agent_id_map[agent.unique_id] = agent

    def _create_regions(self, regional_data):
        for data in regional_data:
            agent = RegionalAgent(model=self, **data)
            self.schedule.add(agent)
            self.agent_id_map[agent.unique_id] = agent

    def _create_governments(self):
        # Create one federal and a few state governments for simplicity
        federal_gov = GovernmentAgent(self.next_id(), self, level='federal')
        self.schedule.add(federal_gov)
        self.agent_id_map[federal_gov.unique_id] = federal_gov
        for i in range(self.num_governments - 1):
            state_gov = GovernmentAgent(self.next_id(), self, level='state')
            self.schedule.add(state_gov)
            self.agent_id_map[state_gov.unique_id] = state_gov

    def step(self):
        """Advance the model by one step."""
        # Clear job board at the beginning of each step
        self.job_board = []
        self.schedule.step()
        self.datacollector.collect(self)
