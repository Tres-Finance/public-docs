# TRES Dashboard Module

This documentation covers the Overview page tabs and the widgets within each tab, including background and product context so PMs, engineers, and users understand what it shows, why it matters, and how to use it.

- Routes: `src/router/routes/index.ts` → `/overview/:id?`
- Overview page: `src/pages/overview/OverviewPage.vue`
- Tab controls: `src/pages/overview/overview-cards/top-section/OverviewTabs.vue`
- Data API: `src/pages/overview/overview.api.ts`
- GraphQL: `src/graphql/queries/overview.ts`

---

## Tabs overview and visibility

- **General**: Always visible. High-level summary and key actions.
- **Positions**: Visible when DeFi positions exist for the org.
- **Staking activity**: Visible when staking activity feature/flag is enabled.
- **Alert center**: Always visible.
- **Cost basis**: Visible when the org has configured cost-basis currencies; data is shown when current currency matches configured currencies.
- **Reconciliation**: Visible when the org has entities configured to reconcile with.
- **Multi Entity**: Visible when multi-entity is enabled for the org.
- **Vested Assets**: Visible when the org has vested assets configured.

---

## Widget background and context

This section gives product/background context for each widget so PMs, engineers, and users understand what it shows, why it matters, and how to use it.

### General tab

#### Net Worth Over Time (`NetworthWrapper.vue`)
- **Background**: Tracks organization net worth across time to reveal trends, regime shifts, and correlation with operations or market cycles.
- **Context**: Use to answer "Are we growing?" "When did our net worth change and by how much?" Export for board updates and monthly reporting.
- **Data**: `DailyNetworth.vue` (time series) + `NetworthBreakdown.vue` (drivers). API: `fetchOverviewNetworth`

#### Top Section (`TopSection.vue`)
- **Background**: Key metrics summary with quick actions and filters.
- **Context**: First thing users see - provides immediate insight into current state and available actions.
- **Data**: Aggregated metrics from multiple sources

#### Actions Section (`ActionsSection.vue`)
- **Background**: Quick access to common operations and workflows.
- **Context**: Reduces friction for frequent tasks like creating transactions, generating reports, or managing accounts.
- **Data**: Action buttons with permission checks

#### Flow Chart (`FlowChart.vue`)
- **Background**: Visual representation of cash flows and transaction patterns.
- **Context**: Helps identify flow patterns, bottlenecks, and unusual activity. Useful for operational analysis.
- **Data**: Transaction flow data with time-based aggregation

#### Top Wallets (`TopWallets.vue`)
- **Background**: Shows highest-value wallets and their current balances.
- **Context**: Quick overview of wallet distribution and concentration. Helps with risk management and operational planning.
- **Data**: Wallet balance data sorted by value

#### Exposure Section (`ExposureSection.vue`)
- **Background**: Risk exposure analysis across different asset classes and platforms.
- **Context**: Critical for risk management, compliance, and strategic decision-making.
- **Data**: Asset allocation and exposure calculations

#### Asset Distribution (`AssetDistribution.vue`)
- **Background**: Pie chart or similar visualization of asset allocation.
- **Context**: Portfolio composition at a glance. Essential for rebalancing decisions and risk assessment.
- **Data**: Asset balance data with categorization

#### DeFi Breakdown (`DefiBreakdown.vue`)
- **Background**: DeFi protocol exposure and yield analysis.
- **Context**: Understanding DeFi risk and yield optimization opportunities.
- **Data**: DeFi position data with protocol categorization

#### Top Positions (`TopPositions.vue`)
- **Background**: Largest DeFi positions by value or yield.
- **Context**: Concentration risk analysis and position management.
- **Data**: DeFi position data sorted by value

#### Rewards Claimed (`RewardsClaimed.vue`)
- **Background**: Historical rewards and yield tracking.
- **Context**: Performance measurement and yield optimization analysis.
- **Data**: Historical rewards data with time series

#### Under Delegation (`UnderDelegationCard.vue`)
- **Background**: Staking delegation status and optimization opportunities.
- **Context**: Maximizing staking rewards and identifying underutilized assets.
- **Data**: Staking delegation data with optimization suggestions

#### Staking Rewards (`StakingRewardsWrapper.vue`)
- **Background**: Comprehensive staking performance and yield analysis.
- **Context**: Staking strategy optimization and performance tracking.
- **Data**: Staking data with yield calculations and trends

#### Notifications (`Notifications.vue`)
- **Background**: System alerts and important updates.
- **Context**: Staying informed about critical events, errors, or opportunities.
- **Data**: Notification data with priority and categorization

#### Reconciliation (`Reconciliation.vue`)
- **Background**: Data reconciliation status and discrepancies.
- **Context**: Ensuring data accuracy and identifying sync issues.
- **Data**: Reconciliation status data with discrepancy details

#### Multi Entity (`MultiEntity.vue`)
- **Background**: Multi-entity organization management and consolidation.
- **Context**: Managing complex organizational structures and consolidated reporting.
- **Data**: Entity data with consolidation rules

#### Vested Assets (`VestedAssets.vue`)
- **Background**: Vesting schedule tracking and management.
- **Context**: Understanding vesting timelines and future cash flows.
- **Data**: Vesting schedule data with timeline visualization

#### Cost Basis (`CostBasis.vue`)
- **Background**: Tax and accounting cost basis tracking.
- **Context**: Tax reporting, P&L calculations, and accounting compliance.
- **Data**: Cost basis data with tax lot tracking

---

## Technical Implementation

### Data Flow
1. **GraphQL Queries**: Data fetched via Apollo Client from BFF service
2. **API Layer**: `overview.api.ts` handles data transformation and caching
3. **Component Layer**: Vue components consume data and handle user interactions
4. **State Management**: Pinia stores manage application state

### Key Dependencies
- Vue 3 with Composition API
- Apollo Client for GraphQL
- Chart.js for data visualization
- Tailwind CSS for styling
- TypeScript for type safety

### Performance Considerations
- Lazy loading for heavy components
- Data caching and memoization
- Virtual scrolling for large datasets
- Optimized re-rendering with Vue's reactivity system

