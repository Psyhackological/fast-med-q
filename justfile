
alias id := install_dependencies
install_dependencies:
  poetry install

alias av := active_virtual
active_virtual:
  poetry shell

alias ra := run_app
run_app:
  poetry run python main.py

set dotenv-load
alias rc := run_container
run_container:
  @echo podman run -d --name $CONTAINER_NAME --env-file '.env' -p $PORT:$PORT $CONTAINER
  podman run -d --name $CONTAINER_NAME --env-file '.env' -p $PORT:$PORT $CONTAINER

