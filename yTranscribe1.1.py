import transcribe
#from transcribe import *
# --- GET SAMPLE TRANSRIPTION FROM FILE TO PROCESS
ImportFile = "yTranscribe\sample.txt"
ExportFile = r'yTranscribe\Converted.txt'
Sample = open(ImportFile, 'r').read()
print(Sample) #Display original in terminal

# --- PROCESS SAMPLE AND OUTPUT
#Processed = yTranscribe(Sample)
Processed = transcribe.yTranscribe(Sample)
print(Processed)

# Export result to file
with open(ExportFile, 'w') as Export:
    Export.write(Processed)
Export.close
#msgBox("Exported to converted.txt")