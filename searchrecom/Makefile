TAG = latest

build-image:
	docker build -t nameko/nameko-searchrecom:$(TAG) ./searchrecom

docker-tag:
	docker tag nameko/nameko-searchrecom:$(TAG) \
	nameko/nameko-searchrecom:$(TAG)

push-image:
	docker push nameko/nameko-searchrecom:$(TAG)