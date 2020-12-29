# DragonTools

## Webservice apps that let's you do common enumeration on your file

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
|stegsolve|check rgb spectrum|

### progress

- [ ] laporan
    - [ ] pembagian tugas
- [ ] produk
    - [ ] frontend
    - [ ] backend
        - [x] file upload
        - [ ] general
            - [x] file
            - [ ] exiftool
                - [x] output
                - [ ] table view
            - [ ] binwalk
                - [x] output
                - [ ] table view
            - [ ] foremost
            - [ ] virustotal
                - [x] output
                - [ ] list view
            - [ ] hash sums
                - [x] output
                - [ ] table view
            - [ ] strings
                - [x] output
                - [ ] search
                - [ ] preview
                - [ ] full output download
            - [ ] xxd
                - [x] output
                - [ ] search
                - [ ] preview
                - [ ] full output download
        - [ ] image
            - [ ] steghide
            - [ ] zsteg
            - [x] pngcheck
            - [ ] stegsolve (???)
        - [ ] misc
            - [ ] tshark
                - [ ] output
                - [ ] search
                - [ ] preview
                - [ ] full output download

#### known issues

##### frontend
- card colors are temporary, either make it random everytime, or static
##### backend
- uploaded files are never deleted
