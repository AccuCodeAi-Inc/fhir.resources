from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/BackboneType
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import datatype, fhirtypes


class BackboneType(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Base for datatypes that can carry modifier extensions.
    Base definition for the few data types that are allowed to carry modifier
    extensions.
    """

    __resource_type__ = "BackboneType"

    modifierExtension: typing.List[fhirtypes.ExtensionType] | None = Field(  # type: ignore
        default=None,
        alias="modifierExtension",
        title="Extensions that cannot be ignored even if unrecognized",
        description=(
            "May be used to represent additional information that is not part of "
            "the basic definition of the element and that modifies the "
            "understanding of the element in which it is contained and/or the "
            "understanding of the containing element's descendants. Usually "
            "modifier elements provide negation or qualification. To make the use "
            "of extensions safe and managable, there is a strict set of governance "
            "applied to the definition and use of extensions. Though any "
            "implementer can define an extension, there is a set of requirements "
            "that SHALL be met as part of the definition of the extension. "
            "Applications processing a resource are required to check for modifier "
            "extensions.  Modifier extensions SHALL NOT change the meaning of any "
            "elements on Resource or DomainResource (including cannot change the "
            "meaning of modifierExtension itself)."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``BackboneType`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``BackboneType`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]
