
deps:
	@which jq || ( which brew && brew install jq || which apt-get && apt-get install jq || which yum && yum install jq || which choco && choco install jq)
	@which aws || pip install awscli

deploy: clean deps
	mkdir -p template/publish
	aws cloudformation validate-template --template-body fileb://template/template.yaml
	aws cloudformation package --template-file template/template.yaml --s3-bucket $(BUCKET_NAME) --s3-prefix divvy-up/template --output-template-file template/publish/template.yaml
	aws cloudformation deploy --template-file template/publish/template.yaml --stack-name $(STACK_NAME) --parameter-overrides `cat parameters/template.json | jq -c --raw-output '.[] | [.ParameterKey + "=" + .ParameterValue] | @tsv'` --capabilities CAPABILITY_NAMED_IAM
	make clean

clean:
	@echo "--> Cleaning up from previous deployment."
	rm -rf code/publish
	rm -rf template/publish
	@echo ""
