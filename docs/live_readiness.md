# Live readiness

- **Project:** YieldGuard Liquidity Rail
- **Track:** Uniswap Agentic Finance
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:21+00:00`

## Trust boundaries

- **Uniswap** — `rest_json` — Quote swaps and bounded liquidity moves.
- **Lido** — `contract_call` — Route staking yield through guarded treasury actions.
- **Bankr Gateway** — `rest_json` — Route inference through cost-aware model selection.
- **Filecoin** — `file_upload` — Persist proofs, logs, and evidence bundles offchain.
- **Celo** — `contract_call` — Settle stablecoin-native transfers on Celo rails.
- **MetaMask Delegations** — `contract_call` — Enforce delegation scopes, expiries, and intent envelopes.
- **PayWithLocus** — `rest_json` — Create bounded subaccounts and controlled spend flows.
- **Bond.credit** — `rest_json` — Journal bounded trades and credit-profile updates.

## Offline-ready partner paths

- **Lido** — prepared_contract_call
- **Filecoin** — prepared_filecoin_bundle
- **Celo** — prepared_contract_call
- **MetaMask Delegations** — prepared_contract_call

## Live-only partner blockers

- **Uniswap**: UNISWAP_API_KEY, UNISWAP_QUOTE_URL — https://developers.uniswap.org/
- **Bankr Gateway**: BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL — https://bankr.bot/
- **PayWithLocus**: LOCUS_API_KEY, LOCUS_PAYMENT_URL — https://docs.locus.finance/
- **Bond.credit**: GMX_ORDER_URL, BOND_CREDIT_PROFILE_URL — https://bond.credit/

## Highest-sensitivity actions

- `bankr_gateway_compute_route` — Bankr Gateway — Use Bankr Gateway for a bounded action in this repo.
- `metamask_delegations_delegate_scope` — MetaMask Delegations — Use MetaMask Delegations for a bounded action in this repo.
- `bond_credit_credit_trade` — Bond.credit — Use Bond.credit for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for UniswapExecutionGuard.
- Run python3 scripts/run_agent.py to produce a dry run for uniswap_agent.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
