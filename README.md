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
        - [ ] font gedein
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
                - [ ] output
            - [ ] virustotal
                - [x] output
                - [ ] list view
            - [ ] hash sums
                - [x] output
                - [ ] table view
            - [ ] strings
                - [x] output
                - [ ] pake overflow: scroll
            - [ ] xxd
                - [x] output
                - [ ] pake overflow: scroll
        - [ ] image
            - [ ] steghide
            - [x] zsteg
            - [x] pngcheck
            - [ ] stegsolve (???)
        - [ ] misc
            - [ ] tshark
                - [ ] output
                - [ ] pake overflow: scroll
        - [ ] donate

#### known issues

##### frontend
- card colors are temporary, either make it random everytime, or static
- font kekecilan / terlalu datar
##### backend
- uploaded files are never deleted
