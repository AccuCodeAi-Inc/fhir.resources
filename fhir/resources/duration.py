from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Duration
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from . import quantity


class Duration(quantity.Quantity):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A length of time.
    """

    __resource_type__ = "Duration"

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``Duration`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "value", "comparator", "unit", "system", "code"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``Duration`` according to specification,
        with preserving the original sequence order.
        """
        return ["value", "comparator", "unit", "system", "code"]
