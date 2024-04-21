package main

deny[msg] {
	input.kind == "Deployment"
	endswith(input.spec.template.spec.containers[_].image, ":latest")
	msg = "No images tagged latest"
}

deny[msg] {
  input.kind == "Deployment"
  not input.spec.selector.matchLabels.app

  msg := "Containers must provide app label for pod selectors"
}
