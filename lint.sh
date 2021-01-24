WHITE='\033[0m'
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)

print_success() {
  echo -e "${GREEN}$1${WHITE}"
}

print_error() {
  echo -e "${RED}$1${WHITE}"
}

print_warn() {
  echo -e "${YELLOW}$1${WHITE}"
}

print_success "Running black..."
if ! black --check -v --diff --color -S src; then
  print_error "Black errors found! Run auto-formatter? (y/n)"
  read -r option
  if [ "$option" == "y" ]; then
    black -S src
  else
    print_warn "Black code style skipped!"
  fi
else
  print_success "Done black!"
fi

print_success 'Running pylint...'
pylint src --rcfile=.pylintrc
print_success 'Done pylint!'

print_success 'Running pycodestyle...'
pycodestyle --exclude=migrations --max-line-length=100 src
print_success 'Done pycodestyle!'
