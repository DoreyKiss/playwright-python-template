docker-pull-pw:
	docker pull mcr.microsoft.com/playwright/python:v1.51.0-noble

docker-build-pw:
	docker build -t my-playwright-poetry .

docker-setup:
	make docker-pull-pw
	make docker-build-pw

docker-cleanup:
	docker rmi my-playwright-poetry || true
	docker system prune
	docker volume prune

docker-run-pw-tests:
	mkdir -p test-reports/docker
	docker run --rm \
		--ipc=host \
		--security-opt seccomp=seccomp_profile.json \
		-v $(PWD)/test-reports/docker:/app/test-reports/docker \
 		my-playwright-poetry

docker-pw-debug:
	mkdir -p test-reports/docker
	docker run -d \
		--ipc=host \
		--security-opt seccomp=seccomp_profile.json \
		--name pw-tests \
		-v $(PWD)/test-reports/docker:/app/test-reports/docker \
		my-playwright-poetry

run-local-pw-tests:
	poetry run pytest 

show-local-report:
	open $$(ls -t test-reports/local/report_*.html | head -n 1)

show-docker-report:
	open $$(ls -t test-reports/docker/report_*.html | head -n 1)

