1) How do we launch your API ?
Execute the app/main.py file or run docker compose up -d --build

2) With more time, what would you have done more, or better ? Why ?
- Improve documentation.
- Create a separate Python package for the model.
- Synchr data folder with DVC.
- REST API version.
- Performance testing with locust lib.
- Deploy the model in kubernetes with linkerd integration and traefik proxy
- Create mkdocs website for the package.

3) How would you deploy your application on your favorite cloud provider ?
- Using GitHub Actions or CircleCI in a Digital Ocean kubernetes cluster.

4) How would you speed-up the computation time for large batches of images ?
- Using a kafka queue for example. Moving from a microservices-based architecture to a hybrid architecture