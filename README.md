# the_youtubes
basically everything I ever put on a playlist plus the script I used to convert the spreadsheet data into html


Using this handy tool https://jolantahuba.github.io/YT-Backup/

repo here:
https://github.com/jolantahuba/YT-Backup/ 

I backed up several of my playlists (well it's music, favorites, neat) to csv files.

Then I opened the csvs in LibreOffice and saved them as odf format.

    pip install pandas odfpy
	
(Pandas needed the odfpy engine to read odf files.)

Then I wrote a quick script to dump the spreadsheet data into html ordered lists and copied it all into one file. Here's that file:

https://dustractor.github.io/the_youtubes

