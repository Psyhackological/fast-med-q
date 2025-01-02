
alias i := install_dependencies
install_dependencies:
  uv sync

alias r := run_app
run_app:
  uv run python 'src/main.py'

set dotenv-load

alias pr := podman_run
podman_run:
  @echo podman run -d --name $CONTAINER_NAME --env-file '.env' -p $PORT:$PORT $CONTAINER
  podman run -d --name $CONTAINER_NAME --env-file '.env' -p $PORT:$PORT $CONTAINER


alias ps := podman_start
podman_start:
  @echo podman start $CONTAINER_NAME
  podman start $CONTAINER_NAME
