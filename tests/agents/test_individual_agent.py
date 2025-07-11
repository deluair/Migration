import unittest
from unittest.mock import MagicMock

from src.agents.individual import IndividualAgent
from src.agents.regional import RegionalAgent
from src.simulation.job_market import JobVacancy

class TestIndividualAgent(unittest.TestCase):

    def setUp(self):
        """Set up a mock model and agents for testing."""
        self.mock_model = MagicMock()
        self.mock_model.random = MagicMock()
        self.mock_model.job_board = []

        # Create a dummy agent for testing
        self.agent = IndividualAgent(
            unique_id=1,
            model=self.mock_model,
            age=30,
            education=0.5,
            soc_code="15-1252",
            wage_percentile=0.6,
            current_msa="MSA1",
            housing_costs=1500,
            household_size=2,
            climate_preference=0.7,

            employer_id=None
        )

        # Create mock regional agents
        self.region1 = RegionalAgent(unique_id="MSA1", model=self.mock_model, unemployment_rate=0.1, median_price=300000, wage_growth=0.01, job_openings_rate=0.05, skills_mismatch=0.2, rent_burden=0.4, construction_permits=100, vacancy_rates=0.05, population_growth=0.02, in_migration=0.01, out_migration=0.01, age_distribution={}, gdp_growth=0.02, productivity=1.1, industry_diversification=0.6, startup_density=0.3, minimum_wage=10, right_to_work=True, remote_work_incentives=False, retraining_funding=10000)
        self.region2 = RegionalAgent(unique_id="MSA2", model=self.mock_model, unemployment_rate=0.02, median_price=200000, wage_growth=0.02, job_openings_rate=0.08, skills_mismatch=0.1, rent_burden=0.3, construction_permits=150, vacancy_rates=0.03, population_growth=0.03, in_migration=0.02, out_migration=0.005, age_distribution={}, gdp_growth=0.03, productivity=1.2, industry_diversification=0.7, startup_density=0.4, minimum_wage=12, right_to_work=False, remote_work_incentives=True, retraining_funding=20000)
        
        self.mock_model.agent_id_map = {"MSA1": self.region1, "MSA2": self.region2}
        self.mock_model.schedule.agents = [self.agent, self.region1, self.region2]

    def test_search_for_job_success(self):
        """Test that an unemployed agent finds and accepts a matching job."""
        self.assertFalse(self.agent.is_employed)
        self.assertIsNone(self.agent.employer_id)

        # Add a matching job to the job board
        matching_vacancy = JobVacancy(firm_id=101, soc_code="15-1252", msa="MSA1")
        self.mock_model.job_board.append(matching_vacancy)

        self.agent.search_for_job()

        self.assertTrue(self.agent.is_employed)
        self.assertEqual(self.agent.employer_id, 101)
        self.assertNotIn(matching_vacancy, self.mock_model.job_board)

    def test_search_for_job_no_match(self):
        """Test that an agent remains unemployed if no matching job is found."""
        # Add a non-matching job
        non_matching_vacancy = JobVacancy(firm_id=102, soc_code="29-1141", msa="MSA1")
        self.mock_model.job_board.append(non_matching_vacancy)

        self.agent.search_for_job()

        self.assertFalse(self.agent.is_employed)
        self.assertIn(non_matching_vacancy, self.mock_model.job_board)

    def test_decide_migration_success(self):
        """Test that an agent migrates to a more favorable region."""
        # Rig the random sample to return our desired candidate region
        self.mock_model.random.sample.return_value = [self.region2]
        
        self.assertEqual(self.agent.current_msa, "MSA1")

        self.agent.decide_migration()

        self.assertEqual(self.agent.current_msa, "MSA2")

if __name__ == '__main__':
    unittest.main()
