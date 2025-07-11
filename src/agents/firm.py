import mesa
from ..simulation.job_market import JobVacancy

class FirmAgent(mesa.Agent):
    """
    A firm agent in the simulation.

    Attributes:
        unique_id: Agent's unique identifier.
        model: The model instance the agent belongs to.
        # Characteristics
        industry: The firm's industry.
        size_category: The firm's size category (e.g., small, medium, large).
        age: The firm's age in years.
        remote_work_policy: The firm's policy on remote work.
        ai_adoption_stage: The firm's stage of AI adoption.
        # Economics
        revenue_growth: The firm's revenue growth rate.
        labor_intensity: The firm's labor intensity.
        geographic_footprint: The geographic footprint of the firm.
        automation_investment: The firm's investment in automation.
        # Employment
        total_workers: The total number of workers at the firm.
        layoff_history: The firm's layoff history.
        hiring_projections: The firm's hiring projections.
        wage_structure: The firm's wage structure.
    """
    def __init__(self, unique_id, model, industry, size_category, age, 
                 remote_work_policy, ai_adoption_stage, revenue_growth, 
                 labor_intensity, geographic_footprint, automation_investment, 
                 total_workers, layoff_history, hiring_projections, wage_structure,
                 msa):
        super().__init__(unique_id, model)
        # Characteristics
        self.industry = industry
        self.size_category = size_category
        self.age = age
        self.remote_work_policy = remote_work_policy
        self.ai_adoption_stage = ai_adoption_stage
        # Economics
        self.revenue_growth = revenue_growth
        self.labor_intensity = labor_intensity
        self.geographic_footprint = geographic_footprint
        self.automation_investment = automation_investment
        # Employment
        self.total_workers = total_workers
        self.layoff_history = layoff_history
        self.hiring_projections = hiring_projections
        self.wage_structure = wage_structure
        # Location
        self.msa = msa
        # Employment tracking
        self.employees = []

    def step(self):
        """
        The agent's step function, called once per step of the simulation.
        """
        self.layoff_logic()
        self.post_job_vacancy()

    def layoff_logic(self):
        """
        Determines whether to lay off an employee based on AI adoption.
        """
        layoff_probabilities = {
            'none': 0.001,  # 0.1% chance
            'early': 0.01,   # 1% chance
            'mature': 0.05    # 5% chance
        }

        prob = layoff_probabilities.get(self.ai_adoption_stage, 0)

        if self.model.random.random() < prob and self.employees:
            # Choose a random employee to lay off
            employee_id = self.model.random.choice(self.employees)
            
            # Find the agent in the model's schedule
            # Note: This is not the most efficient way for large models.
            # A dictionary mapping unique_id to agent would be faster.
            for agent in self.model.schedule.agents:
                if agent.unique_id == employee_id:
                    employee = agent
                    break
            else:
                return # Agent not found

            # Update employee status
            employee.is_employed = False
            employee.employer_id = None

            # Remove employee from firm's list
            self.employees.remove(employee_id)
            self.total_workers -= 1

    def post_job_vacancy(self):
        """
        Post a job vacancy to the model's central job board with some probability.
        Currently, the vacancy's soc_code is chosen at random.
        """
        # 5% chance each step to open a new position
        if self.model.random.random() < 0.05:
            # Choose a random SOC code similar to workforce needs; simplified
            soc_code = f"15-{self.model.random.randint(1000, 2000)}"
            vacancy = JobVacancy(firm_id=self.unique_id, soc_code=soc_code, msa=self.msa)
            self.model.job_board.append(vacancy)

