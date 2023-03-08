async def cancel_all_states_if_they_were(state):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
