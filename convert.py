import sys
import os
import subprocess
import dropbox

ACCESS_TOKEN = os.environ.get('DROPBOX_ACCESS_TOKEN', '')
DROPBOX_FOLDER = os.environ.get('DROPBOX_FOLDER', '')

if not ACCESS_TOKEN:
    print("Error: Missing DROPBOX_ACCESS_TOKEN")
    sys.exit(1)

dbx = dropbox.Dropbox(ACCESS_TOKEN)

# List files in folder
list_path = DROPBOX_FOLDER if DROPBOX_FOLDER else ''
result = dbx.files_list_folder(list_path)

for entry in result.entries:
    # File only
    if not isinstance(entry, dropbox.files.FileMetadata):
        continue
    # Ignore kepub files
    if entry.name.endswith('.kepub.epub'):
        continue
    # Only work with epub files
    if not entry.name.endswith('.epub'):
        continue
    
    file_path = entry.path_display
    file_name = entry.name
    
    print(f'Processing: {file_name}')
    print(f'Original path: {file_path}')
    
    # Download epub from Dropbox
    metadata, response = dbx.files_download(file_path)
    with open(file_name, 'wb') as f:
        f.write(response.content)
    
    # Convert to kepub
    output_name = file_name[:len(file_name) - 5] + '.kepub.epub'
    subprocess.run(['kepubify', '-o', output_name, file_name], check=True)
    
    # Construct paths
    if file_path.startswith('/'):
        parent = os.path.dirname(file_path)
        output_folder = f'{parent}/converted' if parent != '/' else '/converted'
        original_folder = f'{parent}/original' if parent != '/' else '/original'
    else:
        output_folder = '/converted'
        original_folder = '/original'
    
    # Create "converted" subfolder if needed
    try:
        dbx.files_get_metadata(output_folder)
    except:
        dbx.files_create_folder_v2(output_folder)
    
    # Upload kepub to "converted" subfolder
    output_path = f'{output_folder}/{output_name}'
    print(f'Upload path: {output_path}')
    
    with open(output_name, 'rb') as f:
        dbx.files_upload(f.read(), output_path, mode=dropbox.files.WriteMode.overwrite)
    
    # Create "original" subfolder if needed
    try:
        dbx.files_get_metadata(original_folder)
    except:
        dbx.files_create_folder_v2(original_folder)
    
    # Move original to "original" subfolder
    new_path = f'{original_folder}/{file_name}'
    dbx.files_move_v2(file_path, new_path)
    
    print(f'Converted to: {output_path}')
    print(f'Moved original to: {new_path}')

print('Done')
