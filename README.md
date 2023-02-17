# Setup

Install Neo4j or Memgraph

We will just use Memgraph for now. Assuming you have Docker installed, start Memgraph:

    docker run -it -p 7687:7687 -p 7444:7444 -p 3000:3000 -v mg_lib:/var/lib/memgraph memgraph/memgraph-platform

and to stop serv ice:

    docker ps
    docker stop CONTAINER_NAME
