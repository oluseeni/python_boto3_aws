import boto3

ddb_table = boto3.resource('dynamodb')  #DynamoDB method used to call python boto3's DynamoDB resource.

Movies = [                              #Items to be placed in the dynamoDB table created.
    {'Movie_Title': "Jurassic Park", 'Genre': "Action"},
    {'Movie_Title': "The Mummy", 'Genre': "Action Adventure"},
    {'Movie_Title': "Marvel's Avengers", 'Genre': "Action Adventure"},
    {'Movie_Title': "Bullet Train", 'Genre': "Action Comedy"},
    {'Movie_Title': "Spy", 'Genre': "Action Comedy"},
    {'Movie_Title': "Tenet", 'Genre': "Action Thriller"},
    {'Movie_Title': "Grown Ups", 'Genre': "Comedy"},
    {'Movie_Title': "Star Wars", 'Genre': "Science Fiction"},
    {'Movie_Title': "Just Go With It", 'Genre': "Romantic Comedy"},
    {'Movie_Title': "Blade Runner", 'Genre': "Thriller"},
    ]
    
table = ddb_table.Table("wk14_movies_table")
with table.batch_writer() as batch:         #Iteration used to put Items from my list variable into the dynamoDB table.
    for Movie_Title in Movies:
        batch.put_item(Item = Movie_Title)

