# YieldGuard Liquidity Rail

- **Repo:** https://github.com/CrystallineButterfly/Synthesis-Uniswap-AgenticFinance
- **Primary track:** Uniswap Agentic Finance
- **Overlap targets:** Lido stETH Treasury, Bankr Gateway, Filecoin, Celo, MetaMask Delegations, PayWithLocus, Bond.credit
- **Primary contract:** UniswapExecutionGuard
- **Primary operator module:** uniswap_agent
- **Live TxIDs:** PENDING
- **ERC-8004 registrations:** PENDING
- **Demo link:** docs/demo_video_script.md

An agentic liquidity rail that only deploys approved yield into swaps, hooks-aware liquidity moves, and cross-chain settlement with dry-run receipts.

## Track evidence

- `artifacts/onchain_intents/lido_yield_route.json`
- `artifacts/filecoin/0x119ba7c4db56bd384237b1454e13137966e653b2adcb50864801085aafcdf1ae.json`
- `artifacts/onchain_intents/celo_payment_settle.json`
- `artifacts/onchain_intents/metamask_delegations_delegate_scope.json`

## Latest verification

```json
{
  "status": "verified",
  "project_name": "YieldGuard Liquidity Rail",
  "track": "Uniswap Agentic Finance",
  "plan_id": "0x119ba7c4db56bd384237b1454e13137966e653b2adcb50864801085aafcdf1ae",
  "simulation_hash": "0xd485cd7c1c2524a6f6d2d269012cd7a127d8531b8435695d17d0b3d75a80641c",
  "execution_status": "offline_prepared",
  "tx_ids": [],
  "artifact_paths": [
    "artifacts/onchain_intents/lido_yield_route.json",
    "artifacts/filecoin/0x119ba7c4db56bd384237b1454e13137966e653b2adcb50864801085aafcdf1ae.json",
    "artifacts/onchain_intents/celo_payment_settle.json",
    "artifacts/onchain_intents/metamask_delegations_delegate_scope.json"
  ],
  "partner_statuses": {
    "Uniswap": "awaiting_credentials",
    "Lido": "prepared_contract_call",
    "Bankr Gateway": "awaiting_credentials",
    "Filecoin": "prepared_filecoin_bundle",
    "Celo": "prepared_contract_call",
    "MetaMask Delegations": "prepared_contract_call",
    "PayWithLocus": "awaiting_credentials",
    "Bond.credit": "awaiting_credentials"
  },
  "created_at": "2026-03-19T03:52:21+00:00"
}
```
