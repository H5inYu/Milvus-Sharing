# Setup
1. `cp docker-compose.yml.sample docker-compose.yml`
2. Fill in your OPENAI_API_KEY in docker-compose.yml
3. In terminal: `docker-compose up -d`
4. Go to 127.0.0.1:10000

# Structure
- Basic Operation
    1. Provide all the basic operations of Milvus. Including create/delete collection, insert/delete data, search/query for data
- Image Search
    1. Provide sample code to easily insert image data into Milvus and make query to search similar images
- Text Search
    1. Provide sample code to embed article to vectors and insert into Milvus. 
    2. Provide navie RAG steps 