# DragonTools

## Webapp that let's you do common analysis on your files

### Feature

|name|usage|
|:---:|:---:|
|file|to check what exactly your file is|
|exiftool|to check the metadata of your file|
|binwalk|to check if there is a hidden file inside|
|foremost|to extract the hidden file|
|strings|to check hidden string text|
|hashsum|integrity check|
|hexdump|simple check of what your file is made of|
|tshark|check your network|
|steghide|extract hidden message on your image file|
|pngcheck|test PNG image files for corruption, display size, type, compression info|
|zsteg|check for hidden message in lsb or msb|

### progress

- [ ] laporan
    - [ ] screenshots
- [ ] produk
    - [x] frontend
        - [x] font gedein
        - [x] warna yg konsisten
    - [ ] backend
        - [x] file upload
        - [ ] general
            - [x] file
            - [x] exiftool
                - [x] output
                - [x] table view
            - [x] binwalk
                - [x] output
                - [x] table view
            - [ ] foremost
                - [ ] output
            - [x] virustotal
                - [x] output
                - [x] list view
            - [x] hash sums
                - [x] output
                - [x] table view
            - [x] strings
                - [x] output
                - [x] pake overflow: scroll
            - [x] xxd
                - [x] output
                - [x] pake overflow: scroll
        - [ ] image
            - [ ] steghide
            - [x] zsteg
            - [x] pngcheck
        - [x] misc
            - [x] tshark
                - [x] output
                - [x] pake overflow: scroll
        - [x] donate

#### known issues

##### frontend
- currently none
##### backend
- uploaded files are never deleted
