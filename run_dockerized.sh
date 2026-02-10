docker build -t flights-mcp:latest .
docker run -d --name flights-mcp -p 8000:8000 flights-mcp:latest
