from src.simulation.model import MigrationModel

# Model parameters
N_INDIVIDUALS = 50
N_FIRMS = 10
N_REGIONS = 5
N_GOVERNMENTS = 2  # 1 federal, 1 state

def run_simulation(steps=10):
    """
    Initializes and runs the migration simulation.
    """
    # Create the model
    model = MigrationModel(n_individuals=N_INDIVIDUALS, 
                           n_firms=N_FIRMS, 
                           n_regions=N_REGIONS, 
                           n_governments=N_GOVERNMENTS)

    # Run the simulation for a specified number of steps
    print(f"Running simulation for {steps} steps...")
    for i in range(steps):
        model.step()
        print(f"Step {i+1} completed.")

    print("Simulation finished.")

    # Collect and print data
    model_data = model.datacollector.get_model_vars_dataframe()
    agent_data = model.datacollector.get_agent_vars_dataframe()

    print("\n--- Simulation Results ---")
    print("Model-level data:")
    print(model_data)

    print("\nAgent-level data (last step):")
    # Filter for the last step and drop agents with no data (e.g., government)
    last_step_data = agent_data.loc[agent_data.index.get_level_values('Step').max()]
    print(last_step_data.dropna(how='all').head())

    # Example analysis: count unemployed agents at the end
    # Example analysis: calculate unemployment rate from model data
    final_employed_count = model_data.iloc[-1]['Employed']
    total_individuals = len(last_step_data[last_step_data['IsEmployed'].notna()])
    if total_individuals > 0:
        unemployment_rate = (1 - (final_employed_count / total_individuals)) * 100
        print(f"\nFinal unemployment rate: {unemployment_rate:.2f}%")

if __name__ == "__main__":
    run_simulation()
