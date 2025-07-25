from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/EnrollmentRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class EnrollmentRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Enrollment request.
    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """

    __resource_type__ = "EnrollmentRequest"

    coverage: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="coverage",
        title="Insurance information",
        description="Reference to the program or plan identification, underwriter or payor.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Coverage"],
        },
    )

    created: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="created",
        title="Creation date",
        description="The date when this resource was created.",
        json_schema_extra={
            "element_property": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_created", title="Extension field for ``created``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Business Identifier",
        description="The Response business identifier.",
        json_schema_extra={
            "element_property": True,
        },
    )

    insurer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="insurer",
        title="Target",
        description="The Insurer who is target  of the request.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    organization: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="organization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the services rendered to the"
            " patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    provider: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="provider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="subject",
        title="The subject of the Products and Services",
        description="Patient Resource.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``EnrollmentRequest`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "status",
            "created",
            "insurer",
            "provider",
            "organization",
            "subject",
            "coverage",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``EnrollmentRequest`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "meta", "implicitRules", "status"]
