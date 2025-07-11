# Migration

## AI-Driven Economic Displacement and Geographic Mobility Simulation Framework

### Project Overview

This repository contains a comprehensive economic simulation modeling the complex dynamics of AI-induced job displacement and subsequent internal migration patterns across the United States (2024-2030). The simulation is grounded in real-world data showing that 14% of workers have already experienced AI-related job displacement, with 40% of employers anticipating workforce reductions between 2025-2030 due to AI automation.

### Core Research Questions

1. **Economic Displacement Patterns**: How do varying rates of AI adoption across industries and regions create heterogeneous displacement pressures that influence migration decisions?

2. **Migration Response Heterogeneity**: What demographic, educational, and occupational characteristics determine whether displaced workers relocate versus retrain locally, given that 77% of AI-related jobs require master's degrees and 18% require doctoral degrees?

3. **Geographic Arbitrage Dynamics**: How do cost-of-living differentials, remote work opportunities, and regional economic policies influence destination choices, particularly the observed Sun Belt migration patterns and suburban shifts?

4. **Regional Economic Equilibrium**: What are the long-term implications for sending and receiving regions when high-skill workers concentrate in AI-resilient metros while leaving AI-vulnerable manufacturing and service communities?

5. **Policy Intervention Efficacy**: How effective are targeted interventions like relocation subsidies (e.g., Tulsa Remote's $10,000 grants) versus retraining programs in mitigating displacement-induced economic disruption?

### Simulation Architecture

#### Multi-Agent Framework
- **Individual Agents**: 500,000 synthetic workers with detailed demographic, educational, occupational, and financial profiles
- **Firm Agents**: 50,000 companies across sectors with varying AI adoption curves and labor demand functions
- **Regional Agents**: 384 Metropolitan Statistical Areas with distinct economic structures and policy environments
- **Government Agents**: Federal, state, and local entities implementing displacement mitigation policies

#### Economic Displacement Module

**AI Penetration Rates by Occupation**:
- Finance/Data Analysis: 67% task automation potential
- Sales Representatives: 67% task automation potential
- Market Research Analysts: 53% task automation potential
- Manufacturing: 2 million workers displaced by 2025
- Managerial Roles: 9-21% automation risk

**Displacement Timing Model**: Implements "gradually then suddenly" pattern where displacement accelerates during economic downturns (40% recession probability in 2025)

**Sectoral Heterogeneity**: Incorporates that larger enterprises are twice as likely to adopt AI compared to smaller firms, creating spatial clustering of displacement

#### Migration Decision Framework

**Financial Constraints Model**:
- Liquid savings distributions by demographic cohort
- Moving cost functions ($5,000-$25,000 range with distance and household size adjustments)
- Income replacement expectations in destination markets
- Housing affordability calculations (remote work enables 20% of workers to afford previously unattainable locations)

**Social Network Effects**:
- Family proximity preferences weighted by age and marital status
- Professional network density in potential destinations
- Community tie strength degradation functions

**Labor Market Integration Probabilities**:
- Skills transferability matrices across metro areas
- Remote work feasibility (20% of workers plan to relocate in 2025, with 49% choosing suburban destinations)
- Industry cluster co-location benefits

#### Geographic Economic Models

**Regional Classification System**:
- **Tech Hubs**: SF Bay Area, Seattle, Austin, Boston (high AI creation, selective displacement)
- **Traditional Manufacturing**: Rust Belt metros (high vulnerability to AI automation)
- **Sun Belt Growth**: Miami (+30% software workers), Orlando, San Antonio, San Diego (rapid tech worker influx)
- **Emerging Tech**: Madison WI, Provo UT, Lincoln NE (university-anchored growth)
- **Rural/Small Metro**: Limited AI adoption but constrained absorption capacity

**Cost Structure Modeling**:
- Housing cost indices with supply elasticity parameters
- Local wage premiums/discounts by occupation
- State and local tax variations affecting net migration benefits

### Synthetic Dataset Generation

#### Individual-Level Microdata (n=500,000)
```
Demographics: age, education, race/ethnicity, marital_status, household_size, homeownership
Occupation: soc_code, industry_naics, ai_exposure_index, wage_percentile, tenure
Location: current_msa, commute_distance, housing_costs, local_network_strength
Financial: liquid_savings, debt_levels, equity_holdings, unemployment_benefits_eligible
Preferences: climate_preference, urban_rural_preference, family_proximity_weight
```

#### Firm-Level Data (n=50,000)
```
Characteristics: industry, size_category, age, remote_work_policy, ai_adoption_stage
Economics: revenue_growth, labor_intensity, geographic_footprint, automation_investment
Employment: total_workers, layoff_history, hiring_projections, wage_structure
```

#### Metro-Level Panel Data (384 MSAs × 84 months)
```
Labor_Markets: unemployment_rate, wage_growth, job_openings_rate, skills_mismatch
Housing: median_price, rent_burden, construction_permits, vacancy_rates  
Demographics: population_growth, in_migration, out_migration, age_distribution
Economics: gdp_growth, productivity, industry_diversification, startup_density
Policy: minimum_wage, right_to_work, remote_work_incentives, retraining_funding
```

### Economic Mechanisms and Behavioral Models

#### Displacement Response Heterogeneity
- **Age-Stratified Responses**: 52% of workers aged 18-24 express career concerns about AI, versus lower concern among older workers approaching retirement
- **Education-Income Interactions**: High-skilled workers with transferable skills more likely to relocate; mid-skilled workers more likely to retrain locally
- **Gender-Occupation Intersections**: 80% of women work in occupations with high AI exposure versus 60% of men

#### Spatial Equilibrium Dynamics
- **Agglomeration Benefits**: Knowledge spillovers and thick labor markets in tech hubs
- **Congestion Costs**: Housing price appreciation and quality-of-life degradation in high-growth metros
- **Regional Multiplier Effects**: Local spending impacts from in-migrant human capital

#### Financial Frictions and Liquidity Constraints
- **Moving Cost Distribution**: Calibrated to Consumer Expenditure Survey data with regional adjustments
- **Credit Access Variations**: FICO score distributions affecting ability to secure housing in destination markets
- **Unemployment Benefit Portability**: State-specific duration and replacement rate variations

### Policy Simulation Modules

#### Relocation Incentive Programs
- **Cash Grant Models**: Tulsa Remote-style programs with $10,000 housing purchase incentives
- **Tax Credit Schemes**: Federal and state moving expense deductions with income phase-outs
- **Infrastructure Investment**: Broadband expansion enabling rural remote work adoption

#### Workforce Transition Support
- **Retraining Program Targeting**: Analysis of 375 million workers globally requiring significant retraining by 2030
- **Income Support Duration**: Extended unemployment benefits for AI-displaced workers
- **Job Matching Services**: Public-private partnerships for skills-based placement

#### Regional Development Strategies
- **Innovation District Creation**: Public investment in tech-oriented economic development
- **University-Industry Partnerships**: Leveraging higher education for economic transformation
- **Place-Based Hiring Preferences**: Local content requirements in government contracting

### Advanced Analytical Features

#### Economic Impact Assessment
- **Welfare Distribution Analysis**: Gini coefficient evolution across regions and demographic groups
- **Fiscal Impact Modeling**: Tax base changes in sending versus receiving jurisdictions
- **Productivity Growth Decomposition**: AI adoption benefits versus human capital mobility effects

#### Network Analysis and Spillover Effects
- **Migration Flow Networks**: Graph theory applications to identify migration corridors and hub destinations
- **Knowledge Diffusion Patterns**: How displaced tech workers transfer skills to emerging regions
- **Social Capital Erosion**: Community capacity degradation in high out-migration areas

#### Scenario Planning and Sensitivity Analysis
- **AI Development Trajectories**: Modeling different rates of capability advancement and deployment speed
- **Economic Shock Integration**: Recession timing and severity effects on displacement-migration coupling
- **Policy Package Optimization**: Multi-objective optimization across equity, efficiency, and regional development goals

### Data Sources and Calibration

#### Primary Economic Data
- **Bureau of Labor Statistics**: Current Population Survey, Occupational Employment Statistics, Job Openings and Labor Turnover Survey
- **Census Bureau**: American Community Survey migration flows, County Business Patterns
- **BEA Regional Accounts**: Metro-level GDP, income, and employment data

#### AI and Technology Adoption
- McKinsey Digital surveys on enterprise AI deployment
- World Economic Forum Future of Jobs reports
- Industry-specific automation studies and expert surveys

#### Migration and Housing
- Remote work relocation surveys
- Tech worker migration studies from Bay Area and other tech hubs
- National Association of Realtors housing market data

### Implementation and Technical Requirements

#### Computational Architecture
- **Simulation Engine**: Agent-based modeling framework (Mesa/NetLogo/SUMO hybrid)
- **Optimization Backend**: Multi-objective genetic algorithms for policy scenario optimization
- **Data Pipeline**: ETL processes for real-time economic indicator integration
- **Visualization Framework**: Interactive dashboards for regional impact assessment

#### Validation and Robustness Testing
- **Historical Backtesting**: 2020-2024 pandemic-induced migration pattern replication
- **Cross-Sectional Validation**: Comparison against established migration models (gravity, intervening opportunities)
- **Sensitivity Analysis**: Monte Carlo simulations across parameter uncertainty ranges

### Expected Outcomes and Applications

#### Academic Research Contributions
- **Spatial Economics**: New insights into technology-driven migration and regional development
- **Labor Economics**: Heterogeneous displacement response modeling with policy implications
- **Urban/Regional Planning**: Evidence base for adaptive place-based economic development strategies

#### Policy Decision Support
- **Federal Workforce Policy**: Targeted interventions for the emerging "White-Collar Recession of 2025"
- **State Economic Development**: Regional competitive positioning in the AI economy
- **Local Government Planning**: Infrastructure and service provision for migration flows

#### Private Sector Applications
- **Real Estate Investment**: Predictive modeling for housing demand shifts
- **Workforce Planning**: Corporate location strategy optimization
- **Economic Development**: Public-private partnership design for talent attraction

This simulation framework represents a critical tool for understanding one of the defining economic transformations of our era: how artificial intelligence reshapes not just what work we do, but fundamentally where we do it and how regional economies adapt to these profound changes.