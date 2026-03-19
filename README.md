# YieldGuard Liquidity Rail

- **Repo:** [Synthesis-Uniswap-AgenticFinance](https://github.com/CrystallineButterfly/Synthesis-Uniswap-AgenticFinance)
- **Primary track:** Uniswap Agentic Finance
- **Category:** trading
- **Primary contract:** `UniswapExecutionGuard`
- **Primary module:** `uniswap_agent`
- **Submission status:** audited and offline-demo ready; optional live partner credentials unlock network execution.

## What this repo does

An agentic liquidity rail that only deploys approved yield into swaps, hooks-aware liquidity moves, and cross-chain settlement with dry-run receipts.

## Why this build matters

Python agents watch Uniswap and partner signals, assemble bounded rebalance plans, and record dry-run hashes before any spend. A policy contract enforces targets, caps, and cooldowns while demo scripts outline how real swaps, bridge legs, and settlement receipts will be attached once API keys and wallets are loaded.

## Submission fit

- **Primary track:** Uniswap Agentic Finance
- **Overlap targets:** Lido stETH Treasury, Bankr Gateway, Filecoin, Celo, MetaMask Delegations, PayWithLocus, Bond.credit
- **Partners covered:** Uniswap, Lido, Bankr Gateway, Filecoin, Celo, MetaMask Delegations, PayWithLocus, Bond.credit

## Idea shortlist

1. Autonomous Cross-Chain Arbitrage Swarm
2. Hooks-Aware Yield Rebalancer
3. Proof-of-Liquidity Treasury Agent

## System graph

```mermaid
flowchart TD
    Signals[Discover signals]
    Planner[Agent runtime]
    DryRun[Dry-run artifact]
    Contract[UniswapExecutionGuard policy contract]
    Verify[Verify and render submission]
    Signals --> Planner --> DryRun --> Contract --> Verify
    Contract --> uniswap[Uniswap]
    Contract --> lido[Lido]
    Contract --> bankr_gateway[Bankr Gateway]
    Contract --> filecoin[Filecoin]
    Contract --> celo[Celo]
    Contract --> metamask_delegations[MetaMask Delegations]
```

## Repository contents

| Path | What it contains |
| --- | --- |
| `src/` | Shared policy contracts plus the repo-specific wrapper contract. |
| `script/Deploy.s.sol` | Foundry deployment entrypoint for the policy contract. |
| `agents/` | Python runtime, project spec, env handling, and partner adapters. |
| `scripts/` | Terminal entrypoints for run, demo planning, and submission rendering. |
| `docs/` | Architecture, credentials, security notes, and demo steps. |
| `submissions/` | Generated `synthesis.md` snippet for this repo. |
| `test/` | Foundry tests for the Solidity control layer. |
| `tests/` | Python tests for runtime and project context. |
| `agent.json` | Submission-facing agent manifest. |
| `agent_log.json` | Local execution log and status trail. |

## Autonomy loop

1. Discover signals relevant to the repo track and its overlap targets.
2. Build a bounded plan with per-action and compute caps.
3. Persist a dry-run artifact before any live execution.
4. Enforce onchain policy through the guarded contract wrapper.
5. Verify outputs, update receipts, and render submission material.

## Current readiness

- **Latest verification:** `verified` at `2026-03-19T03:52:21+00:00`
- **Execution mode:** `offline_prepared`
- **Offline-prepared partners:** Lido (prepared_contract_call), Filecoin (prepared_filecoin_bundle), Celo (prepared_contract_call), MetaMask Delegations (prepared_contract_call)
- **Live credential blockers:** Uniswap, Bankr Gateway, PayWithLocus, Bond.credit
- **Audit docs:** `docs/audit.md`, `docs/live_readiness.md`

## Most sensitive actions

- `bankr_gateway_compute_route` (Bankr Gateway, high)
- `metamask_delegations_delegate_scope` (MetaMask Delegations, high)
- `bond_credit_credit_trade` (Bond.credit, high)

## Live blocker details

- **Uniswap** — UNISWAP_API_KEY, UNISWAP_QUOTE_URL — https://developers.uniswap.org/
- **Bankr Gateway** — BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL — https://bankr.bot/
- **PayWithLocus** — LOCUS_API_KEY, LOCUS_PAYMENT_URL — https://docs.locus.finance/
- **Bond.credit** — GMX_ORDER_URL, BOND_CREDIT_PROFILE_URL — https://bond.credit/

## Latest evidence artifacts

- `artifacts/onchain_intents/lido_yield_route.json`
- `artifacts/filecoin/0x119ba7c4db56bd384237b1454e13137966e653b2adcb50864801085aafcdf1ae.json`
- `artifacts/onchain_intents/celo_payment_settle.json`
- `artifacts/onchain_intents/metamask_delegations_delegate_scope.json`

## Security controls

- Admin-managed allowlists for targets and selectors.
- Per-action caps, daily caps, cooldown windows, and a principal floor.
- Reporter-only receipt anchoring and proof attachment.
- Env-only secrets; no committed private keys or partner tokens.
- Pause switch plus dry-run-first execution flow.

## Action catalog

| Action | Partner | Purpose | Max USD | Sensitivity |
| --- | --- | --- | --- | --- |
| `uniswap_quote_route` | Uniswap | Use Uniswap for a bounded action in this repo. | $220 | medium |
| `lido_yield_route` | Lido | Use Lido for a bounded action in this repo. | $200 | medium |
| `bankr_gateway_compute_route` | Bankr Gateway | Use Bankr Gateway for a bounded action in this repo. | $10 | high |
| `filecoin_proof_store` | Filecoin | Use Filecoin for a bounded action in this repo. | $20 | medium |
| `celo_payment_settle` | Celo | Use Celo for a bounded action in this repo. | $150 | low |
| `metamask_delegations_delegate_scope` | MetaMask Delegations | Use MetaMask Delegations for a bounded action in this repo. | $2 | high |
| `paywithlocus_subaccount_pay` | PayWithLocus | Use PayWithLocus for a bounded action in this repo. | $120 | medium |
| `bond_credit_credit_trade` | Bond.credit | Use Bond.credit for a bounded action in this repo. | $90 | high |

## Local terminal flow (Anvil + Sepolia)

```bash
export SEPOLIA_RPC_URL=https://sepolia.infura.io/v3/YOUR_KEY
anvil --fork-url "$SEPOLIA_RPC_URL" --chain-id 11155111
cp .env.example .env
# keep private keys only in .env; TODO.md stays local-only too
forge script script/Deploy.s.sol --rpc-url "$RPC_URL" --broadcast
python3 scripts/run_agent.py
python3 scripts/render_submission.py
```

## Commands

```bash
python3 -m unittest discover -s tests
forge test
python3 scripts/run_agent.py
python3 scripts/plan_live_demo.py
python3 scripts/render_submission.py
```

## Credentials

| Partner | Variables | Docs |
| --- | --- | --- |
| Uniswap | UNISWAP_API_KEY, UNISWAP_QUOTE_URL | https://developers.uniswap.org/ |
| Lido | RPC_URL | https://docs.lido.fi/ |
| Bankr Gateway | BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL | https://bankr.bot/ |
| Filecoin | FILECOIN_API_TOKEN, FILECOIN_UPLOAD_URL | https://docs.filecoin.cloud/ |
| Celo | CELO_RPC_URL | https://docs.celo.org/ |
| MetaMask Delegations | RPC_URL | https://docs.metamask.io/delegation-toolkit/ |
| PayWithLocus | LOCUS_API_KEY, LOCUS_PAYMENT_URL | https://docs.locus.finance/ |
| Bond.credit | GMX_ORDER_URL, BOND_CREDIT_PROFILE_URL | https://bond.credit/ |

## Live demo plan

1. Copy .env.example to .env and fill the required keys.
2. Deploy the contract with forge script script/Deploy.s.sol --broadcast for UniswapExecutionGuard.
3. Run python3 scripts/run_agent.py to produce a dry run for uniswap_agent.
4. Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
5. Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
