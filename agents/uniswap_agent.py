"""Project-specific context for YieldGuard Liquidity Rail."""

        from __future__ import annotations

        PROJECT_CONTEXT = {
    "project_name": "YieldGuard Liquidity Rail",
    "track": "Uniswap Agentic Finance",
    "pitch": "An agentic liquidity rail that only deploys approved yield into swaps, hooks-aware liquidity moves, and cross-chain settlement with dry-run receipts.",
    "overlap_targets": [
        "Lido stETH Treasury",
        "Bankr Gateway",
        "Filecoin",
        "Celo",
        "MetaMask Delegations",
        "PayWithLocus",
        "Bond.credit"
    ],
    "goals": [
        "discover a bounded opportunity",
        "plan a dry-run-first action",
        "verify receipts and proofs"
    ]
}


        def seed_targets() -> list[str]:
            """Return the first batch of overlap targets for planning."""
            return list(PROJECT_CONTEXT['overlap_targets'])
