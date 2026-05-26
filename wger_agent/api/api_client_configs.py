#!/usr/bin/env python
from wger_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_weight_configs(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List weight progression configs."""
        return self._list("weight-config", limit=limit, offset=offset, **filters)

    def get_weight_config(self, config_id: int) -> dict:
        """Get a specific weight config."""
        return self._get(f"weight-config/{config_id}")

    def create_weight_config(
        self,
        slot_entry: int,
        iteration: int = 1,
        value: float = 0,
        operation: str = "r",
        step: str = "abs",
        repeat: bool = False,
        **kwargs,
    ) -> dict:
        """Create a weight progression config."""
        data = {
            "slot_entry": slot_entry,
            "iteration": iteration,
            "value": value,
            "operation": operation,
            "step": step,
            "repeat": repeat,
            **kwargs,
        }
        return self._post("weight-config", data=data)

    def update_weight_config(self, config_id: int, **kwargs) -> dict:
        """Update a weight config."""
        return self._patch(f"weight-config/{config_id}", data=kwargs)

    def delete_weight_config(self, config_id: int) -> bool:
        """Delete a weight config."""
        return self._delete(f"weight-config/{config_id}")

    def get_max_weight_configs(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List max weight configs."""
        return self._list("max-weight-config", limit=limit, offset=offset, **filters)

    def create_max_weight_config(self, slot_entry: int, **kwargs) -> dict:
        """Create a max weight config."""
        return self._post(
            "max-weight-config", data={"slot_entry": slot_entry, **kwargs}
        )

    def get_repetitions_configs(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List repetitions configs."""
        return self._list("repetitions-config", limit=limit, offset=offset, **filters)

    def create_repetitions_config(
        self,
        slot_entry: int,
        iteration: int = 1,
        value: float = 0,
        operation: str = "r",
        step: str = "abs",
        repeat: bool = False,
        **kwargs,
    ) -> dict:
        """Create a repetitions config."""
        data = {
            "slot_entry": slot_entry,
            "iteration": iteration,
            "value": value,
            "operation": operation,
            "step": step,
            "repeat": repeat,
            **kwargs,
        }
        return self._post("repetitions-config", data=data)

    def update_repetitions_config(self, config_id: int, **kwargs) -> dict:
        """Update a repetitions config."""
        return self._patch(f"repetitions-config/{config_id}", data=kwargs)

    def delete_repetitions_config(self, config_id: int) -> bool:
        """Delete a repetitions config."""
        return self._delete(f"repetitions-config/{config_id}")

    def get_max_repetitions_configs(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List max repetitions configs."""
        return self._list(
            "max-repetitions-config", limit=limit, offset=offset, **filters
        )

    def create_max_repetitions_config(self, slot_entry: int, **kwargs) -> dict:
        """Create a max repetitions config."""
        return self._post(
            "max-repetitions-config", data={"slot_entry": slot_entry, **kwargs}
        )

    def get_sets_configs(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List sets configs."""
        return self._list("sets-config", limit=limit, offset=offset, **filters)

    def create_sets_config(
        self,
        slot_entry: int,
        iteration: int = 1,
        value: float = 0,
        operation: str = "r",
        step: str = "abs",
        repeat: bool = False,
        **kwargs,
    ) -> dict:
        """Create a sets config."""
        data = {
            "slot_entry": slot_entry,
            "iteration": iteration,
            "value": value,
            "operation": operation,
            "step": step,
            "repeat": repeat,
            **kwargs,
        }
        return self._post("sets-config", data=data)

    def update_sets_config(self, config_id: int, **kwargs) -> dict:
        """Update a sets config."""
        return self._patch(f"sets-config/{config_id}", data=kwargs)

    def delete_sets_config(self, config_id: int) -> bool:
        """Delete a sets config."""
        return self._delete(f"sets-config/{config_id}")

    def get_max_sets_configs(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List max sets configs."""
        return self._list("max-sets-config", limit=limit, offset=offset, **filters)

    def create_max_sets_config(self, slot_entry: int, **kwargs) -> dict:
        """Create a max sets config."""
        return self._post("max-sets-config", data={"slot_entry": slot_entry, **kwargs})

    def get_rest_configs(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List rest time configs."""
        return self._list("rest-config", limit=limit, offset=offset, **filters)

    def create_rest_config(
        self,
        slot_entry: int,
        iteration: int = 1,
        value: float = 0,
        operation: str = "r",
        step: str = "abs",
        repeat: bool = False,
        **kwargs,
    ) -> dict:
        """Create a rest time config."""
        data = {
            "slot_entry": slot_entry,
            "iteration": iteration,
            "value": value,
            "operation": operation,
            "step": step,
            "repeat": repeat,
            **kwargs,
        }
        return self._post("rest-config", data=data)

    def update_rest_config(self, config_id: int, **kwargs) -> dict:
        """Update a rest config."""
        return self._patch(f"rest-config/{config_id}", data=kwargs)

    def delete_rest_config(self, config_id: int) -> bool:
        """Delete a rest config."""
        return self._delete(f"rest-config/{config_id}")

    def get_max_rest_configs(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List max rest configs."""
        return self._list("max-rest-config", limit=limit, offset=offset, **filters)

    def create_max_rest_config(self, slot_entry: int, **kwargs) -> dict:
        """Create a max rest config."""
        return self._post("max-rest-config", data={"slot_entry": slot_entry, **kwargs})

    def get_rir_configs(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List RiR configs."""
        return self._list("rir-config", limit=limit, offset=offset, **filters)

    def create_rir_config(
        self,
        slot_entry: int,
        iteration: int = 1,
        value: float = 0,
        operation: str = "r",
        step: str = "abs",
        repeat: bool = False,
        **kwargs,
    ) -> dict:
        """Create a RiR config."""
        data = {
            "slot_entry": slot_entry,
            "iteration": iteration,
            "value": value,
            "operation": operation,
            "step": step,
            "repeat": repeat,
            **kwargs,
        }
        return self._post("rir-config", data=data)

    def update_rir_config(self, config_id: int, **kwargs) -> dict:
        """Update a RiR config."""
        return self._patch(f"rir-config/{config_id}", data=kwargs)

    def delete_rir_config(self, config_id: int) -> bool:
        """Delete a RiR config."""
        return self._delete(f"rir-config/{config_id}")

    def get_max_rir_configs(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List max RiR configs."""
        return self._list("max-rir-config", limit=limit, offset=offset, **filters)

    def create_max_rir_config(self, slot_entry: int, **kwargs) -> dict:
        """Create a max RiR config."""
        return self._post("max-rir-config", data={"slot_entry": slot_entry, **kwargs})
