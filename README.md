# fasta_converter

A small Python script that converts SnapGene `.dna` files to FASTA (`.fa`).

## How it works

The script looks in each immediate subdirectory of the folder it lives in, converts every `.dna` file it finds using [snapgene_reader](https://github.com/IsaacLuo/SnapGeneFileReader), and writes a `.fa` file next to the original. The FASTA header is the file name without its extension. It then prints the length of each converted sequence.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Place your `.dna` files in a subfolder next to the script:

```
fasta_converter/
├── fasta_converter.py
└── my_plasmids/
    ├── plasmid1.dna
    └── plasmid2.dna
```

Then run:

```bash
python fasta_converter.py
```

Example output:

```
Converted files:
  my_plasmids/plasmid1.dna: 5432
  my_plasmids/plasmid2.dna: 7210
```

Files that fail to convert are reported as warnings and skipped.

## License

Released under the [MIT License](LICENSE).

## Notes

Sequence files (`.dna`, `.fa`, `.fasta`) are git-ignored so that data is not committed to the repository.
