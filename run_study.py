# Lightweight Machine Learning for IoT Intrusion Detection
# An Extended Accuracy · Efficiency · Robustness · Adversarial Study on IoTID20
# Training script for reproducing all results

import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description='IoTID20 IDS Study - V3')
    parser.add_argument('--fast', action='store_true', help='Fast mode (fewer seeds, smaller samples)')
    parser.add_argument('--no-cross-dataset', action='store_true', help='Skip cross-dataset validation')
    parser.add_argument('--notebook', action='store_true', help='Convert to notebook and run with jupyter')
    args = parser.parse_args()

    if args.fast:
        os.environ['FAST_MODE'] = '1'
    if args.no_cross_dataset:
        os.environ['RUN_CROSS_DATASET'] = '0'

    print("=" * 60)
    print("IoTID20 Lightweight IDS Study - V3")
    print("=" * 60)
    print(f"Fast mode: {args.fast}")
    print(f"Cross-dataset: {not args.no_cross_dataset}")
    print()
    print("To run the full analysis, execute the notebook:")
    print("  jupyter notebook notebook/IoTIDS20-V3.ipynb")
    print()
    print("Or run with FAST_MODE for a quick smoke test:")
    print("  FAST_MODE=1 jupyter notebook notebook/IoTIDS20-V3.ipynb")

if __name__ == '__main__':
    main()
