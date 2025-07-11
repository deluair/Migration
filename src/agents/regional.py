import mesa

class RegionalAgent(mesa.Agent):
    """
    A regional agent representing a Metropolitan Statistical Area (MSA).

    Attributes:
        unique_id: Agent's unique identifier (e.g., MSA code).
        model: The model instance the agent belongs to.
        # Labor Markets
        unemployment_rate: The regional unemployment rate.
        wage_growth: The regional wage growth rate.
        job_openings_rate: The rate of job openings in the region.
        skills_mismatch: An index of skills mismatch in the labor market.
        # Housing
        median_price: The median housing price.
        rent_burden: The rent burden for the population.
        construction_permits: The number of new construction permits.
        vacancy_rates: The housing vacancy rates.
        # Demographics
        population_growth: The population growth rate.
        in_migration: The rate of in-migration.
        out_migration: The rate of out-migration.
        age_distribution: The age distribution of the population.
        # Economics
        gdp_growth: The regional GDP growth rate.
        productivity: The regional productivity level.
        industry_diversification: An index of industry diversification.
        startup_density: The density of startups in the region.
        # Policy
        minimum_wage: The local minimum wage.
        right_to_work: Whether the region is in a right-to-work state.
        remote_work_incentives: Incentives for remote workers.
        retraining_funding: Funding available for retraining programs.
    """
    def __init__(self, unique_id, model, unemployment_rate, wage_growth, 
                 job_openings_rate, skills_mismatch, median_price, rent_burden, 
                 construction_permits, vacancy_rates, population_growth, 
                 in_migration, out_migration, age_distribution, gdp_growth, 
                 productivity, industry_diversification, startup_density, 
                 minimum_wage, right_to_work, remote_work_incentives, 
                 retraining_funding):
        super().__init__(unique_id, model)
        # Labor Markets
        self.unemployment_rate = unemployment_rate
        self.wage_growth = wage_growth
        self.job_openings_rate = job_openings_rate
        self.skills_mismatch = skills_mismatch
        # Housing
        self.median_price = median_price
        self.rent_burden = rent_burden
        self.construction_permits = construction_permits
        self.vacancy_rates = vacancy_rates
        # Demographics
        self.population_growth = population_growth
        self.in_migration = in_migration
        self.out_migration = out_migration
        self.age_distribution = age_distribution
        # Economics
        self.gdp_growth = gdp_growth
        self.productivity = productivity
        self.industry_diversification = industry_diversification
        self.startup_density = startup_density
        # Policy
        self.minimum_wage = minimum_wage
        self.right_to_work = right_to_work
        self.remote_work_incentives = remote_work_incentives
        self.retraining_funding = retraining_funding

    def step(self):
        """Update regional indicators based on current state of agents in this region."""
        # Gather individuals in this MSA
        individuals = [a for a in self.model.schedule.agents if hasattr(a, 'current_msa') and a.current_msa == self.unique_id]
        if individuals:
            employed = sum(1 for ind in individuals if ind.is_employed)
            self.unemployment_rate = 1 - (employed / len(individuals))
            # Wage growth simple proxy: average wage_percentile change (placeholder)
            avg_wage = sum(getattr(ind, 'wage_percentile', 0.5) for ind in individuals) / len(individuals)
            # Smooth wage growth
            self.wage_growth = 0.8 * self.wage_growth + 0.2 * (avg_wage - 0.5)
        # Housing vacancy rate adjustment based on construction permits (placeholder)
        self.vacancy_rates = max(0.01, min(0.2, self.vacancy_rates + (self.construction_permits/10000 - 0.05)))
