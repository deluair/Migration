import numpy as np

def generate_firm_data(num_firms, region_ids):
    """
    Generates a list of dictionaries, each representing a firm agent's attributes.

    Args:
        num_firms: The number of firm agents to generate.
        region_ids: A list of regional agent unique_ids (e.g., MSA codes) for location assignment.

    Returns:
        A list of dictionaries with synthetic data for each firm.
    """
    data = []
    for _ in range(num_firms):
        agent_data = {
            # Characteristics
            'industry': np.random.choice(['tech', 'finance', 'manufacturing', 'retail', 'healthcare']),
            'size_category': np.random.choice(['small', 'medium', 'large'], p=[0.6, 0.3, 0.1]),
            'age': np.random.randint(1, 50),
            'remote_work_policy': np.random.choice(['none', 'hybrid', 'full']),
            'ai_adoption_stage': np.random.choice(['none', 'early', 'mature']),
            # Economics
            'revenue_growth': np.random.uniform(-0.05, 0.15),
            'labor_intensity': np.random.uniform(0.2, 0.8),
            'geographic_footprint': np.random.choice(['local', 'national', 'global']),
            'automation_investment': np.random.lognormal(mean=12, sigma=2.0),
            # Employment
            'total_workers': np.random.randint(10, 10000),
            'layoff_history': np.random.choice([True, False]),
            'hiring_projections': np.random.uniform(-0.1, 0.1),
            'wage_structure': np.random.choice(['below_market', 'market_rate', 'above_market']),
            # Location
            'msa': np.random.choice(region_ids),
        }
        data.append(agent_data)
    return data


def generate_regional_data(num_regions):
    """
    Generates a list of dictionaries, each representing a regional agent's attributes.

    Args:
        num_regions: The number of regional agents to generate.

    Returns:
        A list of dictionaries with synthetic data for each region.
    """
    data = []
    for i in range(num_regions):
        agent_data = {
            'unique_id': f'MSA{i+1}',
            # Labor Markets
            'unemployment_rate': np.random.uniform(0.02, 0.1),
            'wage_growth': np.random.uniform(0.01, 0.05),
            'job_openings_rate': np.random.uniform(0.02, 0.08),
            'skills_mismatch': np.random.uniform(0.1, 0.5),
            # Housing
            'median_price': np.random.lognormal(mean=12.5, sigma=0.4),
            'rent_burden': np.random.uniform(0.2, 0.5),
            'construction_permits': np.random.randint(100, 10000),
            'vacancy_rates': np.random.uniform(0.01, 0.15),
            # Demographics
            'population_growth': np.random.uniform(-0.01, 0.03),
            'in_migration': np.random.randint(500, 50000),
            'out_migration': np.random.randint(500, 50000),
            'age_distribution': {'18-34': 0.3, '35-54': 0.4, '55+': 0.3}, # Simplified
            # Economics
            'gdp_growth': np.random.uniform(-0.02, 0.06),
            'productivity': np.random.uniform(0.8, 1.5),
            'industry_diversification': np.random.uniform(0.3, 0.9),
            'startup_density': np.random.uniform(0.001, 0.05),
            # Policy
            'minimum_wage': np.random.uniform(7.25, 20.0),
            'right_to_work': np.random.choice([True, False]),
            'remote_work_incentives': np.random.choice([True, False]),
            'retraining_funding': np.random.lognormal(mean=13, sigma=1.5),
        }
        data.append(agent_data)
    return data

def generate_individual_data(num_individuals, regions):
    """
    Generates a list of dictionaries, each representing an individual agent's attributes.
    
    Args:
        num_individuals: The number of individual agents to generate.
        regions: A list of regional agent unique_ids (e.g., MSA codes) for location assignment.

    Returns:
        A list of dictionaries with synthetic data for each individual.
    """
    data = []
    for _ in range(num_individuals):
        agent_data = {
            # Demographics
            'age': np.random.randint(18, 65),
            'education': np.random.choice(['high_school', 'bachelor', 'master', 'phd'], p=[0.3, 0.5, 0.15, 0.05]),
            'race_ethnicity': np.random.choice(['white', 'black', 'hispanic', 'asian', 'other'], p=[0.6, 0.13, 0.18, 0.06, 0.03]),
            'marital_status': np.random.choice(['single', 'married']),
            'household_size': np.random.randint(1, 5),
            'homeownership': np.random.choice([True, False]),
            # Occupation
            'soc_code': f"15-{np.random.randint(1000, 2000)}",
            'industry_naics': np.random.choice(['54', '62', '44-45', '72', '31-33']),
            'ai_exposure_index': np.random.uniform(0, 1),
            'wage_percentile': np.random.uniform(0.1, 0.99),
            'tenure': np.random.uniform(0, 20),
            # Location
            'current_msa': np.random.choice(regions),
            'commute_distance': np.random.uniform(5, 60),
            'housing_costs': np.random.uniform(800, 5000),
            'local_network_strength': np.random.uniform(0.1, 1.0),
            # Financial
            'liquid_savings': np.random.lognormal(mean=9, sigma=1.5),
            'debt_levels': np.random.lognormal(mean=10, sigma=1.2),
            'equity_holdings': np.random.lognormal(mean=8, sigma=2.0),
            'unemployment_benefits_eligible': np.random.choice([True, False]),
            # Preferences
            'climate_preference': np.random.choice(['warm', 'moderate', 'cold']),
            'urban_rural_preference': np.random.choice(['urban', 'suburban', 'rural']),
            'family_proximity_weight': np.random.uniform(0, 1),
        }
        data.append(agent_data)
    return data
