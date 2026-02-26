# Chokobo  

🇻🇳 [Xem hướng dẫn bằng tiếng Việt](README.vi.md)

A semi-automatic utility to convert `epub` books to `kepub` on Dropbox for Kobo e-readers (`Chokobo` means `for Kobo` in Vietnamese).  

It is labeled "semi-automatic" because after uploading books to Dropbox, you must manually trigger the utility to start the conversion process; it cannot be fully automated.

https://github.com/user-attachments/assets/702c95af-690a-4c23-a448-62c014cdb461

## ✨ Features
Uses GitHub Actions to convert `epub` files on Dropbox into the `kepub` standard, then uploads them back to Dropbox.

**Advantages over other methods::**  
- No need to connect the Kobo to a computer via cable
- No need for complex Calibre setups  
- Books are stored on Dropbox, allowing downloads to the Kobo at any time  
- Can be triggered from any device: PC, smartphone, etc  
- Supports batch conversion of multiple books (more convenient than [send.djazz.se](https://send.djazz.se/))  
- 100% private

**Disadvantages:**  
- Initial setup and configuration involve multiple steps, which may be overwhelming for non-technical users.
- GitHub Actions provides 2,000 free minutes per month
  - Each run takes approximately 1 minute (more for large batches), making it difficult to exceed the limit unless you process an extreme volume of books  
  - Batching multiple books in one run is more time-efficient than running the tool for each individual book  
  - [Click here](../../actions/metrics/usage) to view usage statistics

## Kepub Format
While Kobo supports Epub, the Kepub (Kobo EPUB) format is recommended for several reasons:  

- Kobo uses the Adobe Ebook reader to render Epub files, which is outdated, slow, and lacks features  
- The Kepub reader uses Webkit, supporting modern features and fewer bugs, resulting in superior rendering


## I. Preparation

### Accounts
This utility requires GitHub and Dropbox accounts. Use the following links to create them for free:  
- [Create GitHub account](https://github.com/signup)
- [Create Dropbox account](https://www.dropbox.com/referrals/AAB_nRkqghEm94wvV6A8TNxakMs3Z6qMh3U) (Referral link: installing the Dropbox app via this link grants you and me an extra 500MB of lifetime storage, roughly 100 eBooks)

### Devices
If using Kobo Forma, Sage, Elipsa, Elipsa 2E, or Libra Colour, skip this step as Dropbox support is native.

For other Kobo models, you must install NickelMenu to enable Dropbox

## II. Installation and Configuration

> [!IMPORTANT]
> The terms `Token` or `AccessToken` function as passwords. Do not expose or share them. They grant access to your account data without requiring your account password.

1. Ensure the Kobo is successfully linked to your Dropbox account ([instructions](https://help.kobo.com/hc/en-us/articles/360033830114-Add-books-to-your-eReader-using-Dropbox))

2. Connect the Kobo to a computer.

3. Open the file `.kobo/Kobo/Kobo eReader.conf` using Notepad (Windows) or TextEdit (Mac).  
    > On macOS, if the `.kobo` folder is hidden, press `Cmd + Shift + .` to show hidden folders in Finder

4. Locate the `[DropboxSettings]` section and copy the `AccessToken` value (required for Step 9).
    <br><br>
    > ```ini
    > [DropboxSettings]
    > AccessToken=<COPY THIS VALUE>
    > UserGuideId=...
    > Username=...
    > ```

5. Close the file and disconnect the Kobo  

6. Log in to GitHub and [click this link](https://github.com/new?template_name=chokobo&template_owner=redphx) to copy the tool to your personal account

7. Enter information:
    - **(1) Repository name**: Enter a name for the repository
    - **(2) Configuration**: Select `PRIVATE` to ensure privacy, then click `Create repository`.
    <br><br><div align="center"><img width="787" height="484" alt="image" src="https://github.com/user-attachments/assets/ce1e2725-f64b-4afe-ba18-dc9534c4c8e6" />
</div>

8. In your new repository, navigate to `Settings > Security > Secrets and variables > Actions`, and click `New repository secret` ([direct link](../../settings/secrets/actions/new))
    <br><div align="center"><img width="796" height="570" alt="image" src="https://github.com/user-attachments/assets/d66d9899-59f5-4bc0-b92d-07ca2628ff06" /></div>

9. Enter the following and click `Add secret`:  
    - **(1) Name**: `DROPBOX_ACCESS_TOKEN`  
    - **(2) Secret**: The `AccessToken` value from Step 4  
    <br><div align="center"><img width="792" height="426" alt="image" src="https://github.com/user-attachments/assets/f328fde7-0c80-4b25-aa24-443588177909" />
</div>

Configuration is complete!

## III. Usage: Converting Books

1. Upload `epub` files to the `Apps/Rakuten Kobo` folder in your Dropbox account (do not place them in subfolders):
    <br><div align="center"><img width="634" height="251" alt="image" src="https://github.com/user-attachments/assets/7caa7f8a-0b59-46da-9cbb-79fed62c5bb1" /></div>

2. To run the tool, go to `Actions > Convert books` in your GitHub repository, click `Run workflow`, then click the green `Run workflow` button again ([direct link](../../actions/workflows/convert.yml))
    <br><div align="center"><img width="812" height="615" alt="image" src="https://github.com/user-attachments/assets/8e70062a-7d15-40a6-ba34-1ee6624b24a6" /></div>

3. Refresh the page to monitor status. Upon success, your Dropbox will contain a `converted` folder (with kepub files) and an `original` folder (with the original epubs)
    <br><div align="center"><img width="634" height="251" alt="image" src="https://github.com/user-attachments/assets/fc2306e6-f4eb-43cd-94df-4fda03c93f2e" /></div>

4. Open the Dropbox feature on your Kobo and download the kepub files  

5. Done  

**Tip:** Bookmark the [Workflow URL](../../actions/workflows/convert.yml) from Step 2 for quick access.

To update Chokobo, run the workflow named [`Update Chokobo`](../../actions/workflows/update.yml).
