
alias id := install_dependencies
install_dependencies:
  poetry install

alias av := active_virtual
active_virtual:
  poetry shell

alias ra := run_app
run_app:
  poetry run uvicorn src.api:app --reload

set dotenv-load
alias rc := run_container
run_container:
  @echo podman run -d --name $CONTAINER_NAME --env-file '.env' -p $PORT:$PORT $CONTAINER
  podman run -d --name $CONTAINER_NAME --env-file '.env' -p $PORT:$PORT $CONTAINER


alias sc := start_container
start_container:
  @echo podman start $CONTAINER_NAME
  podman start $CONTAINER_NAME
