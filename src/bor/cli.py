from __future__ import annotations

import argparse

from .metrics import (
    bits_over_random,
    bor_ceiling,
    collapse_lambda,
    random_success_at_least_m,
    random_success_at_least_one,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute random baselines and Bits-over-Random."
    )
    parser.add_argument("--N", type=int, required=True, help="Corpus size.")
    parser.add_argument("--R", type=int, required=True, help="Relevant items in corpus.")
    parser.add_argument("--K", type=int, required=True, help="Items retrieved.")
    parser.add_argument(
        "--observed",
        type=float,
        required=True,
        help="Observed success rate, e.g. 0.82.",
    )
    parser.add_argument(
        "--m",
        type=int,
        default=1,
        help="Success threshold. Default is at least one relevant item.",
    )

    args = parser.parse_args()

    if args.m == 1:
        p_rand = random_success_at_least_one(args.N, args.R, args.K)
    else:
        p_rand = random_success_at_least_m(args.N, args.R, args.K, args.m)

    bor = bits_over_random(args.observed, p_rand)
    ceiling = bor_ceiling(p_rand)
    lam = collapse_lambda(args.N, args.R, args.K)

    print(f"N: {args.N}")
    print(f"R: {args.R}")
    print(f"K: {args.K}")
    print(f"Observed success: {args.observed:.4f}")
    print(f"Random baseline: {p_rand:.4f}")
    print(f"Bits-over-Random: {bor:.4f}")
    print(f"BoR ceiling: {ceiling:.4f}")
    print(f"lambda: {lam:.4f}")

    if p_rand >= 0.95:
        print("warning: random baseline is already near 1.0")
    if lam >= 3:
        print("warning: lambda is in the collapse zone")


if __name__ == "__main__":
    main()