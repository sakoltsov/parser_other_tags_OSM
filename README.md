# parser_other_tags_OSM
transformation of all tags from other_tags OpenStreetMap to table columns


read csv with ID and tags 

save in dataframe - source

create result dataframe with index = ID from source dataframe

parse other tags 

cleaning name tags 

save name and value tags to result dataframe as name tags - columns dataframe, value tags - value dataframe

create string for schema to BigQuery

write result dataframe to csv

write string scheme to txt

*made in jupyter notebook
