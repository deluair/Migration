import unittest
import pandas as pd

from ai_migration_simulation.model.migration_model import MigrationModel

class TestIntegration(unittest.TestCase):

    def test_full_model_run(self):
        """Test a full run of the simulation to ensure all components integrate correctly."""
        # Initialize the model with a small population for a quick test
        model = MigrationModel(
            n_individuals=50, 
            n_firms=10, 
            n_msas=3, 
            max_steps=5
        )

        # Run the simulation
        model.run_model()

        # 1. Check DataCollector Output
        model_df = model.datacollector.get_model_vars_dataframe()
        agent_df = model.datacollector.get_agent_vars_dataframe()

        self.assertIsInstance(model_df, pd.DataFrame, "Model data should be a DataFrame.")
        self.assertFalse(model_df.empty, "Model data should not be empty.")
        self.assertIn('Unemployment Rate', model_df.columns, "Unemployment Rate should be in model data.")

        self.assertIsInstance(agent_df, pd.DataFrame, "Agent data should be a DataFrame.")
        self.assertFalse(agent_df.empty, "Agent data should not be empty.")
        self.assertIn('is_employed', agent_df.columns, "'is_employed' should be in agent data.")

        # 2. Verify Key Simulation Dynamics
        # Check for layoffs: some agents should become unemployed over time
        initial_unemployment = agent_df.loc[0]['is_employed'].value_counts().get(False, 0)
        final_unemployment = agent_df.loc[model.schedule.steps - 1]['is_employed'].value_counts().get(False, 0)
        # With layoffs and hiring, the number could go up or down, but we expect some change
        # This is a weak check, but confirms the state is not static
        self.assertNotEqual(initial_unemployment, final_unemployment, "Employment status should change over time.")

        # Check for migration: some agents should change their MSA
        initial_msas = agent_df.loc[0]['current_msa'].tolist()
        final_msas = agent_df.loc[model.schedule.steps - 1]['current_msa'].tolist()
        self.assertNotEqual(initial_msas, final_msas, "Agent MSAs should change, indicating migration.")

        # 3. Check Job Board Dynamics
        # The job board should have seen some activity
        self.assertGreater(len(model.job_board), 0, "Job board should have vacancies posted during the run.")

if __name__ == '__main__':
    unittest.main()
