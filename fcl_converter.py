import json
import argparse
from FCL.fcl_generator import generate_fcl


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert EPCIS V2 JSON document to Food Chain Lab document')
    parser.add_argument('input', help='Name of the input file to process')
    parser.add_argument('-t', '--tracking', type=str, default='example:prevID', help='Extension name to identify the tracking events')
    parser.add_argument('output', help='Name of the output FCL file')

    args = parser.parse_args()

    print(f"Filename: {args.input}")
    epcis_data = json.load(open(args.input, 'r'))
    generated_fcl = generate_fcl(epcis_data, args.tracking)

    with open(args.output, 'w') as outfile:
        outfile.write(json.dumps(generated_fcl, indent=4))
    print(f"Finished: {args.output}")