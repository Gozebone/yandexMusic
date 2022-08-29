def current_track(client):
    queues = client.queues_list()
    # Последняя проигрываемая очередь всегда в начале списка
    last_queue = client.queue(queues[0].id)

    last_track_id = last_queue.get_current_track()
    last_track = last_track_id.fetch_track()


    artists = ', '.join(last_track.artists_name())
    title = last_track.title
    print(f'Сейчас играет: {artists} - {title}')