# YieldGuard Liquidity Rail

- **Repo:** `Synthesis-Uniswap-AgenticFinance`
- **Primary track:** Uniswap Agentic Finance
- **Category:** trading
- **Submission status:** implementation ready, waiting for credentials and TxIDs.

An agentic liquidity rail that only deploys approved yield into swaps, hooks-aware liquidity moves, and cross-chain settlement with dry-run receipts.

## Selected concept

Python agents watch Uniswap and partner signals, assemble bounded rebalance plans, and record dry-run hashes before any spend. A policy contract enforces targets, caps, and cooldowns while demo scripts outline how real swaps, bridge legs, and settlement receipts will be attached once API keys and wallets are loaded.

## Idea shortlist

1. Autonomous Cross-Chain Arbitrage Swarm
2. Hooks-Aware Yield Rebalancer
3. Proof-of-Liquidity Treasury Agent

## Partners covered

Uniswap, Lido, Bankr Gateway, Filecoin, Celo, MetaMask Delegations, PayWithLocus, Bond.credit

## Architecture

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

## Repository layout

- `src/`: shared policy contracts plus the repo-specific wrapper contract.
- `script/`: Foundry deployment entrypoint.
- `agents/`: Python runtime, partner adapters, and project metadata.
- `scripts/`: CLI utilities for running the loop and rendering submissions.
- `docs/`: architecture, credentials, demo script, and security notes.
- `submissions/`: generated `synthesis.md` snippet for this repo.

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
