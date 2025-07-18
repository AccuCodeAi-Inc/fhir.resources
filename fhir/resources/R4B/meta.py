from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Meta
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class Meta(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Metadata about a resource.
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always
    be associated with version changes to the resource.
    """

    __resource_type__ = "Meta"

    lastUpdated: fhirtypes.InstantType | None = Field(  # type: ignore
        default=None,
        alias="lastUpdated",
        title="When the resource version last changed",
        description="When the resource last changed - e.g. when the version changed.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    lastUpdated__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_lastUpdated", title="Extension field for ``lastUpdated``."
    )

    profile: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        default=None,
        alias="profile",
        title="Profiles this resource claims to conform to",
        description=(
            "A list of profiles (references to "
            "[StructureDefinition](structuredefinition.html#) resources) that this "
            "resource claims to conform to. The URL is a reference to "
            "[StructureDefinition.url](structuredefinition-"
            "definitions.html#StructureDefinition.url)."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    profile__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        default=None, alias="_profile", title="Extension field for ``profile``."
    )

    security: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        default=None,
        alias="security",
        title="Security Labels applied to this resource",
        description=(
            "Security labels applied to this resource. These tags connect specific "
            "resources to the overall security policy and infrastructure."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    source: fhirtypes.UriType | None = Field(  # type: ignore
        default=None,
        alias="source",
        title="Identifies where the resource comes from",
        description=(
            "A uri that identifies the source system of the resource. This provides"
            " a minimal amount of [Provenance](provenance.html#) information that "
            "can be used to track or differentiate the source of information in the"
            " resource. The source may identify another FHIR server, document, "
            "message, database, etc."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_source", title="Extension field for ``source``."
    )

    tag: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        default=None,
        alias="tag",
        title="Tags applied to this resource",
        description=(
            "Tags applied to this resource. Tags are intended to be used to "
            "identify and relate resources to process and workflow, and "
            "applications are not required to consider the tags when interpreting "
            "the meaning of a resource."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    versionId: fhirtypes.IdType | None = Field(  # type: ignore
        default=None,
        alias="versionId",
        title="Version specific identifier",
        description=(
            "The version specific identifier, as it appears in the version portion "
            "of the URL. This value changes when the resource is created, updated, "
            "or deleted."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    versionId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_versionId", title="Extension field for ``versionId``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``Meta`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "versionId",
            "lastUpdated",
            "source",
            "profile",
            "security",
            "tag",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``Meta`` according to specification,
        with preserving the original sequence order.
        """
        return ["versionId", "lastUpdated", "source", "profile", "security", "tag"]
