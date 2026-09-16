#Import modules
from snapgene_reader import snapgene_file_to_seqrecord
import os

if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    root_dir = os.path.dirname(abspath)
    os.chdir(root_dir)

    seqSizesList = []

    # Walk one level of subdirectories only
    for subdir_name in next(os.walk(root_dir))[1]:  # get list of subdirectories
        subdir_path = os.path.join(root_dir, subdir_name)

        for file in os.listdir(subdir_path):
            if file.endswith(".dna"):
                dna_path = os.path.join(subdir_path, file)

                try:
                    readSeqRecord = snapgene_file_to_seqrecord(dna_path)
                    seqRecord = readSeqRecord.seq

                    out_path = os.path.join(subdir_path, file[:-4] + ".fa")
                    with open(out_path, "w") as f:
                        f.write(f">{file[:-4]}\n{seqRecord}")

                    seqSizesList.append(f"{os.path.join(subdir_name, file)}: {len(seqRecord)}")

                except Exception as e:
                    print(f"[warning] Failed to convert {file}: {e}")

    # Print results
    if seqSizesList:
        print("Converted files:")
        for line in seqSizesList:
            print("  " + line)
    else:
        print("No .dna files found in subdirectories.")