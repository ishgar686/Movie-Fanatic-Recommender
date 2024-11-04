mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"igarg@ucsd.edu\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]/n/
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml