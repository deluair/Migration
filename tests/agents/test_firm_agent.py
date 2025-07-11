import unittest
from unittest.mock import MagicMock, patch

from src.agents.firm import FirmAgent
from src.agents.individual import IndividualAgent
from src.simulation.job_market import JobVacancy

class TestFirmAgent(unittest.TestCase):

    def setUp(self):
        """Set up a mock model and agents for testing."""
        self.mock_model = MagicMock()
        self.mock_model.random = MagicMock()
        self.mock_model.job_board = []

        # Create mock employees first, providing all required arguments
        self.employee1 = IndividualAgent(
            unique_id=1, model=self.mock_model, age=30, education=0.5, race_ethnicity='A', marital_status='M',
            household_size=2, homeownership=True, soc_code='15-1252', industry_naics='54', ai_exposure_index=0.8,
            wage_percentile=0.7, tenure=5, current_msa='MSA1', commute_distance=10, housing_costs=1500,
            local_network_strength=0.9, liquid_savings=50000, debt_levels=20000, equity_holdings=10000,
            unemployment_benefits_eligible=True, climate_preference=0.6, urban_rural_preference=0.8,
            family_proximity_weight=0.5, employer_id=101
        )
        self.employee2 = IndividualAgent(
            unique_id=2, model=self.mock_model, age=45, education=0.7, race_ethnicity='B', marital_status='S',
            household_size=1, homeownership=False, soc_code='29-1141', industry_naics='62', ai_exposure_index=0.3,
            wage_percentile=0.8, tenure=10, current_msa='MSA1', commute_distance=20, housing_costs=2000,
            local_network_strength=0.5, liquid_savings=100000, debt_levels=5000, equity_holdings=50000,
            unemployment_benefits_eligible=True, climate_preference=0.4, urban_rural_preference=0.6,
            family_proximity_weight=0.8, employer_id=101
        )
        self.mock_model.schedule.agents = [self.employee1, self.employee2]

        # Correctly instantiate FirmAgent with all required arguments
        self.firm = FirmAgent(
            unique_id=101,
            model=self.mock_model,
            msa="MSA1",
            industry="Tech",
            size_category="medium",
            age=5,
            remote_work_policy=0.5,
            ai_adoption_stage='none',
            revenue_growth=0.03,
            labor_intensity=0.6,
            geographic_footprint="national",
            automation_investment=50000,
            total_workers=2,
            layoff_history=[],
            hiring_projections={},
            wage_structure={}
        )
        self.firm.employees = [self.employee1.unique_id, self.employee2.unique_id]

    def test_layoff_logic(self):
        """Test that an employee is laid off based on AI adoption."""
        self.firm.ai_adoption_stage = 'mature'  # High layoff probability
        self.mock_model.random.random.return_value = 0.01  # Ensure layoff probability check passes
        self.mock_model.random.choice.return_value = self.employee1.unique_id # Choose employee1 to lay off

        self.firm.layoff_logic()

        self.assertFalse(self.employee1.is_employed, "Employee1 should have been laid off")
        self.assertIsNone(self.employee1.employer_id, "Employee1's employer_id should be None")
        self.assertNotIn(self.employee1.unique_id, self.firm.employees, "Employee1 should be removed from firm's employee list")
        self.assertTrue(self.employee2.is_employed, "Employee2 should not have been laid off")

    def test_post_job_vacancy(self):
        """Test that a job vacancy is posted to the job board."""
        self.mock_model.random.random.return_value = 0.01 # Ensure vacancy post check passes
        self.assertEqual(len(self.mock_model.job_board), 0)

        self.firm.post_job_vacancy()

        self.assertEqual(len(self.mock_model.job_board), 1, "A vacancy should have been posted")
        vacancy = self.mock_model.job_board[0]
        self.assertIsInstance(vacancy, JobVacancy)
        self.assertEqual(vacancy.firm_id, self.firm.unique_id)
        self.assertEqual(vacancy.msa, self.firm.msa)

if __name__ == '__main__':
    unittest.main()
