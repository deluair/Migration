import unittest
from unittest.mock import MagicMock

from src.agents.regional import RegionalAgent
from src.agents.individual import IndividualAgent

class TestRegionalAgent(unittest.TestCase):

    def setUp(self):
        """Set up a mock model and agents for testing."""
        self.mock_model = MagicMock()
        self.mock_model.schedule = MagicMock()

        self.region = RegionalAgent(
            unique_id="MSA1", model=self.mock_model, unemployment_rate=0.0, median_price=300000, 
            wage_growth=0.0, job_openings_rate=0.0, skills_mismatch=0.0, rent_burden=0.0, 
            construction_permits=0, vacancy_rates=0.0, population_growth=0.0, in_migration=0.0, 
            out_migration=0.0, age_distribution={}, gdp_growth=0.0, productivity=0.0, 
            industry_diversification=0.0, startup_density=0.0, minimum_wage=0, right_to_work=False, 
            remote_work_incentives=False, retraining_funding=0
        )

        # Create mock individuals for the region
        self.employed_agent = self._create_mock_individual(1, 'MSA1', employer_id=101)
        self.unemployed_agent = self._create_mock_individual(2, 'MSA1', employer_id=None)
        self.other_region_agent = self._create_mock_individual(3, 'MSA2', employer_id=102)
        
        self.mock_model.schedule.agents = [self.region, self.employed_agent, self.unemployed_agent, self.other_region_agent]

    def _create_mock_individual(self, unique_id, msa, employer_id):
        """Helper to create a mock IndividualAgent with necessary attributes."""
        agent = IndividualAgent(
            unique_id=unique_id, model=self.mock_model, age=30, education=0.5, race_ethnicity='A', marital_status='M',
            household_size=2, homeownership=True, soc_code='15-1252', industry_naics='54', ai_exposure_index=0.8,
            wage_percentile=0.7, tenure=5, current_msa=msa, commute_distance=10, housing_costs=1500,
            local_network_strength=0.9, liquid_savings=50000, debt_levels=20000, equity_holdings=10000,
            unemployment_benefits_eligible=True, climate_preference=0.6, urban_rural_preference=0.8,
            family_proximity_weight=0.5, employer_id=employer_id
        )
        # Manually set is_employed for clarity in tests
        agent.is_employed = True if employer_id is not None else False
        return agent

    def test_step_updates_unemployment_rate(self):
        """Test that the regional unemployment rate is updated correctly."""
        # In MSA1, there is 1 employed and 1 unemployed agent out of 2 total.
        # Expected unemployment rate = 1 / 2 = 0.5
        self.region.step()
        self.assertAlmostEqual(self.region.unemployment_rate, 0.5)

if __name__ == '__main__':
    unittest.main()
