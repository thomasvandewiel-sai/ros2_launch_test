FROM recksahr/sony_workflow_containers:latest

COPY entrypoint.sh /entrypoint.sh
COPY rosbag_health_checker.py /rosbag_health_checker.py
COPY optimization_based_action_selection_performance.py /optimization_based_action_selection_performance.py

RUN bash -c 'echo -e end of docker'

ENTRYPOINT ["/entrypoint.sh"]