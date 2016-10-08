FROM piensa/deeplearning

COPY ./bin/jupyter.sh /
RUN chmod +x /jupyter.sh

CMD ["/jupyter.sh"]
