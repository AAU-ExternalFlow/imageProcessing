import os
import subprocess

def generateSubFolder(folderName):
    os.makedirs(folderName, exist_ok=True)


def paraviewResults(aoa_array):
    file_paths = ['/externalflow/imageProcessing/Mesh1.py', '/externalflow/imageProcessing/Mesh2.py', '/externalflow/imageProcessing/Mesh3.py', '/externalflow/imageProcessing/Mesh4.py', '/externalflow/imageProcessing/U1.py', '/externalflow/imageProcessing/U2.py', '/externalflow/imageProcessing/P1.py', '/externalflow/imageProcessing/P2.py']

    # Define the common value
    value = aoa_array[0]

    # Define the lines to replace for each file
    lines_to_replace = {
        '/externalflow/imageProcessing/Mesh1.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (501, "SaveScreenshot('/externalflow/assets/{value}/mesh1.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
        '/externalflow/imageProcessing/Mesh2.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (495, "SaveScreenshot('/externalflow/assets/{value}/mesh2.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
        '/externalflow/imageProcessing/Mesh3.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (495, "SaveScreenshot('/externalflow/assets/{value}/mesh3.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
        '/externalflow/imageProcessing/Mesh4.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (495, "SaveScreenshot('/externalflow/assets/{value}/mesh4.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
        '/externalflow/imageProcessing/U1.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (604, "SaveScreenshot('/externalflow/assets/{value}/U1.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
        '/externalflow/imageProcessing/U2.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (601, "SaveScreenshot('/externalflow/assets/{value}/U2.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
        '/externalflow/imageProcessing/P1.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (539, "SaveScreenshot('/externalflow/assets/{value}/P1.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
        '/externalflow/imageProcessing/P2.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (539, "SaveScreenshot('/externalflow/assets/{value}/P2.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
    }

    for i, value in enumerate(aoa_array):
        previous_value = aoa_array[i - 1] if i > 0 else 0
        print(f"Current value: {value}, Previous value: {previous_value}")

        for file_path in file_paths:
            replacements = lines_to_replace.get(file_path, [])  # Get the replacements for this file
            with open(file_path, 'r') as f:
                lines = f.readlines()

            with open(file_path, 'w') as f:
                for j, line in enumerate(lines, 1):
                    for line_number, new_line in replacements:
                        if j == line_number:
                            f.writelines(new_line.format(value=value))
                            break
                    else:
                        f.writelines(line)

            subprocess.run(['/externalflow/paraview/bin/pvpython', file_path])

