TAG = latest

build-image:
	docker build -t nameko/nameko-example-searchrecom:$(TAG) ./searchrecom

docker-tag:
	docker tag nameko/nameko-example-searchrecom:$(TAG) \
	nameko/nameko-example-searchrecom:$(TAG)

push-image:
	docker push nameko/nameko-example-searchrecom:$(TAG)