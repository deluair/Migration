import mesa

class IndividualAgent(mesa.Agent):
    """
    An individual agent in the simulation.

    Attributes:
        unique_id: Agent's unique identifier.
        model: The model instance the agent belongs to.
        # Demographics
        age: The agent's age.
        education: The agent's education level.
        race_ethnicity: The agent's race or ethnicity.
        marital_status: The agent's marital status.
        household_size: The size of the agent's household.
        homeownership: Whether the agent owns a home.
        # Occupation
        soc_code: Standard Occupational Classification code.
        industry_naics: North American Industry Classification System code.
        ai_exposure_index: Index of exposure to AI displacement.
        wage_percentile: The agent's wage percentile.
        tenure: The agent's job tenure in years.
        # Location
        current_msa: The agent's current Metropolitan Statistical Area.
        commute_distance: The agent's commute distance.
        housing_costs: The agent's housing costs.
        local_network_strength: Strength of the agent's local social network.
        # Financial
        liquid_savings: The agent's liquid savings.
        debt_levels: The agent's debt levels.
        equity_holdings: The agent's equity holdings.
        unemployment_benefits_eligible: Eligibility for unemployment benefits.
        # Preferences
        climate_preference: The agent's preference for climate.
        urban_rural_preference: The agent's preference for urban vs. rural living.
        family_proximity_weight: The weight given to family proximity in decisions.
    """
    def __init__(self, unique_id, model, age, education, race_ethnicity, marital_status,
                 household_size, homeownership, soc_code, industry_naics,
                 ai_exposure_index, wage_percentile, tenure, current_msa,
                 commute_distance, housing_costs, local_network_strength,
                 liquid_savings, debt_levels, equity_holdings,
                 unemployment_benefits_eligible, climate_preference,
                 urban_rural_preference, family_proximity_weight, employer_id=None):
        super().__init__(unique_id, model)
        # Demographics
        self.age = age
        self.education = education
        self.race_ethnicity = race_ethnicity
        self.marital_status = marital_status
        self.household_size = household_size
        self.homeownership = homeownership
        # Occupation
        self.soc_code = soc_code
        self.industry_naics = industry_naics
        self.ai_exposure_index = ai_exposure_index
        self.wage_percentile = wage_percentile
        self.tenure = tenure
        # Location
        self.current_msa = current_msa
        self.commute_distance = commute_distance
        self.housing_costs = housing_costs
        self.local_network_strength = local_network_strength
        # Financial
        self.liquid_savings = liquid_savings
        self.debt_levels = debt_levels
        self.equity_holdings = equity_holdings
        self.unemployment_benefits_eligible = unemployment_benefits_eligible
        # Preferences
        self.climate_preference = climate_preference
        self.urban_rural_preference = urban_rural_preference
        self.family_proximity_weight = family_proximity_weight

        # Employment Status
        self.is_employed = True if employer_id is not None else False
        self.employer_id = employer_id

    def step(self):
        """
        The agent's step function, called once per step of the simulation.
        """
        # 1. Job search if unemployed
        if not self.is_employed:
            self.search_for_job()
        # 2. Occasional migration decision
        if self.model.random.random() < 0.02:  # 2% chance to evaluate migration each step
            self.decide_migration()

    def decide_migration(self):
        """Simple migration logic: consider moving to region with lower unemployment and cheaper housing."""
        # Get current region stats
        current_region = self.model.agent_id_map.get(self.current_msa)
        if not current_region:
            return
        # Gather alternative regions (exclude current)
        all_regions = [agent for agent in self.model.schedule.agents if isinstance(agent, type(current_region)) and agent.unique_id != self.current_msa]
        if not all_regions:
            return
        sample_size = min(5, len(all_regions))
        candidate_regions = self.model.random.sample(all_regions, k=sample_size)

        best_region = current_region
        best_score = current_region.unemployment_rate + (current_region.median_price / 1e6)
        for region in candidate_regions:
            score = region.unemployment_rate + (region.median_price / 1e6)
            if score < best_score:
                best_score = score
                best_region = region
        if best_region.unique_id != self.current_msa:
            # Migrate
            self.current_msa = best_region.unique_id
            # Simple update: adjust housing_costs proportionally
            self.housing_costs = best_region.median_price / 12  # approx monthly

    def search_for_job(self):
        """
        An unemployed agent looks for a job by checking firms that are hiring.
        """
        # Search the model's job board for vacancies matching the agent's SOC code
        matching_vacancies = [v for v in self.model.job_board if v.soc_code == self.soc_code and v.msa == self.current_msa]
        if not matching_vacancies:
            # Broaden search to any MSA if none found in current location
            matching_vacancies = [v for v in self.model.job_board if v.soc_code == self.soc_code]

        if matching_vacancies:
            vacancy = self.model.random.choice(matching_vacancies)
            employer = self.model.agent_id_map.get(vacancy.firm_id)
            if employer:
                # Accept the job
                self.is_employed = True
                self.employer_id = employer.unique_id
                employer.employees.append(self.unique_id)
                employer.total_workers += 1

                # Remove vacancy from job board
                self.model.job_board.remove(vacancy)
